"""Met à jour la section Avancement du README à partir des cases cochées de ROADMAP.md
et du nombre d'entrées de journal. Lancé automatiquement par /session fin."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

roadmap = (ROOT / "ROADMAP.md").read_text()

phases: list[dict] = []
current = None
for line in roadmap.splitlines():
    m = re.match(r"^## (Phase \d+) — (.+?) \(semaines ([\d-]+)\)", line)
    if m:
        current = {"num": m.group(1), "title": m.group(2), "done": 0, "total": 0}
        phases.append(current)
        continue
    if current is not None:
        if line.startswith("- [x]"):
            current["done"] += 1
            current["total"] += 1
        elif line.startswith("- [ ]"):
            current["total"] += 1

sessions_done = len(
    [p for p in (ROOT / "journal").glob("*.md") if re.match(r"\d{4}-\d{2}-\d{2}", p.name)]
)
SESSIONS_TOTAL = 240  # 48 semaines x 5 sessions


def bar(done: int, total: int, width: int = 20) -> str:
    filled = round(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled)


total_done = sum(p["done"] for p in phases)
total_items = sum(p["total"] for p in phases)
pct_global = round(100 * total_done / total_items) if total_items else 0
pct_sessions = round(100 * sessions_done / SESSIONS_TOTAL)

lines = [
    "## 📊 Avancement",
    "",
    f"**Global : `{bar(total_done, total_items)}` {pct_global}%** — {total_done}/{total_items} jalons de la roadmap",
    "",
    f"**Sessions : {sessions_done}/{SESSIONS_TOTAL}** (`{bar(sessions_done, SESSIONS_TOTAL)}` {pct_sessions}%)",
    "",
    "| Phase | Progression | |",
    "|---|---|---|",
]
for p in phases:
    pct = round(100 * p["done"] / p["total"]) if p["total"] else 0
    status = "✅" if pct == 100 else ("🔵" if p["done"] else "⚪")
    lines.append(f"| {status} {p['num']} — {p['title']} | `{bar(p['done'], p['total'])}` | {pct}% |")

block = "\n".join(lines)

readme_path = ROOT / "README.md"
readme = readme_path.read_text()
new = re.sub(
    r"<!-- PROGRESS:START -->.*<!-- PROGRESS:END -->",
    f"<!-- PROGRESS:START -->\n{block}\n<!-- PROGRESS:END -->",
    readme,
    flags=re.S,
)
readme_path.write_text(new)
print(f"README mis à jour — global {pct_global}%, {sessions_done} sessions au journal.")
