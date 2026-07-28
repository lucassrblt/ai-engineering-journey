"""Régénère calendar/formation.ics avec les 14 prochains jours :
chaque session en semaine (7h-8h) porte le titre et le programme précis de la
prochaine session non faite (déduite du nombre d'entrées de journal), le samedi
(10h-12h) porte la revue hebdo. Lancé automatiquement par /session fin.

Le calendrier doit être AJOUTÉ PAR URL (abonnement), pas importé, pour se mettre à jour."""
import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DAYS_AHEAD = 14


def sessions_in_order() -> list[tuple[str, str, list[str]]]:
    """Toutes les sessions de tous les SESSIONS.md, dans l'ordre des phases."""
    units = []
    for f in sorted(ROOT.glob("phases/phase-*/SESSIONS.md")):
        blocks = re.split(r"^### ", f.read_text(), flags=re.M)[1:]
        for block in blocks:
            header, _, body = block.partition("\n")
            m = re.match(r"(S[\d.]+(?:-S[\d.]+)?) — (.+)", header.strip())
            if not m:
                continue
            sid, title = m.group(1), m.group(2)
            body = body.split("\n## ")[0]
            tasks = []
            for line in body.splitlines():
                line = line.strip()
                if line.startswith("- "):
                    tasks.append(re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line))
            # un header "S4.4-S4.5" couvre deux sessions
            for _ in range(2 if "-S" in sid else 1):
                units.append((sid, title, tasks))
    return units


def journal_count() -> int:
    return len([p for p in (ROOT / "journal").glob("*.md") if re.match(r"\d{4}-\d{2}-\d{2}", p.name)])


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def fold(line: str) -> str:
    parts = []
    while len(line) > 73:
        parts.append(line[:73])
        line = " " + line[73:]
    parts.append(line)
    return "\r\n".join(parts)


def event(uid: str, date: dt.date, h1: str, h2: str, summary: str, description: str) -> list[str]:
    d = date.strftime("%Y%m%d")
    return [
        "BEGIN:VEVENT",
        f"UID:{uid}-{d}@ai-engineering-journey",
        f"DTSTAMP:{dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')}",
        f"DTSTART;TZID=Europe/Paris:{d}T{h1}",
        f"DTEND;TZID=Europe/Paris:{d}T{h2}",
        fold(f"SUMMARY:{esc(summary)}"),
        fold(f"DESCRIPTION:{esc(description)}"),
        "BEGIN:VALARM",
        "ACTION:DISPLAY",
        "DESCRIPTION:Session de formation dans 10 minutes",
        "TRIGGER:-PT10M",
        "END:VALARM",
        "END:VEVENT",
    ]


def main() -> None:
    remaining = sessions_in_order()[journal_count():]
    intro = "cd ~/Desktop/dev/ai-engineering-journey && claude puis taper /session\n\n"
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//ai-engineering-journey//formation//FR",
        "CALSCALE:GREGORIAN",
        "X-WR-CALNAME:Formation AI Engineering",
        "REFRESH-INTERVAL;VALUE=DURATION:PT4H",
        "BEGIN:VTIMEZONE",
        "TZID:Europe/Paris",
        "BEGIN:DAYLIGHT",
        "TZOFFSETFROM:+0100",
        "TZOFFSETTO:+0200",
        "TZNAME:CEST",
        "DTSTART:19700329T020000",
        "RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU",
        "END:DAYLIGHT",
        "BEGIN:STANDARD",
        "TZOFFSETFROM:+0200",
        "TZOFFSETTO:+0100",
        "TZNAME:CET",
        "DTSTART:19701025T030000",
        "RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU",
        "END:STANDARD",
        "END:VTIMEZONE",
    ]
    i = 0
    now = dt.datetime.now()
    for offset in range(DAYS_AHEAD):
        day = dt.date.today() + dt.timedelta(days=offset)
        if offset == 0 and now.hour >= (12 if day.weekday() == 5 else 8):
            continue  # la session du jour est déjà passée : on planifie à partir de demain
        if day.weekday() < 5:  # lundi-vendredi : session de 1h
            if i >= len(remaining):
                break
            sid, title, tasks = remaining[i]
            i += 1
            desc = intro + f"{sid} — {title}\n\n" + "\n".join(tasks)
            lines += event("session", day, "070000", "080000", f"🎯 {sid} — {title}", desc[:1500])
        elif day.weekday() == 5:  # samedi : revue + session longue
            desc = (
                intro
                + "10h00-10h45 : /session revue — bilan de la semaine, cocher la roadmap, "
                + "préparer la semaine suivante.\n10h45-12h00 : session longue — mini-projet "
                + "de la semaine ou rattrapage."
            )
            lines += event("revue", day, "100000", "120000", "📊 Revue hebdo + session longue", desc)
    lines.append("END:VCALENDAR")
    (ROOT / "calendar" / "formation.ics").write_text("\r\n".join(lines) + "\r\n")
    print(f"Calendrier régénéré : prochaine session = {remaining[0][0] if remaining else 'aucune'}, "
          f"{i} sessions planifiées sur {DAYS_AHEAD} jours.")


if __name__ == "__main__":
    main()
