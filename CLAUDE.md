# Contexte du projet — AI Engineering Journey

## Qui je suis

Lucas, développeur fullstack JS/TS (3 ans d'expérience : Vue/React/Next en front, Express/Nest en back), notions DevOps (Docker, CI/CD GitHub Actions, VPS, GCP). En Master 1 (formation CTO/Tech Lead), 3e année d'alternance. Au quotidien je n'écris plus de code : j'orchestre des agents Claude Code (backlogs, contexte, choix de modèles). Je ne connais pas ou peu Python.

## L'objectif de ce repo

Me former **1h30/jour (5 sessions/semaine + revue hebdo)** pendant 12 mois pour transitionner vers un poste **AI Engineer / GenAI Engineer** (construire des produits sur les API de LLM : RAG, agents, evals — PAS du ML classique/entraînement de modèles). Ce repo est à la fois mon curriculum, mon journal et une pièce de mon portfolio (visible recruteurs).

## Décisions déjà prises (ne pas re-débattre sans nouvelle info)

- **École "produit sur modèles de fondation"** (roadmap.sh, Chip Huyen), PAS l'école data-science (pas de NumPy/pandas/scikit-learn/PyTorch, pas de maths poussées, pas de certifications cloud). Justification : c'est ce que demandent les offres 2026 ; le ML classique a un mauvais ROI pour ces rôles.
- **Python quand même** (malgré mon profil TS) : exigé par les offres, écosystème evals Python-first, et taper un nouveau langage reconstruit le muscle du code que j'ai perdu.
- **Règle d'or : pendant les sessions de formation, je tape le code moi-même.** Claude sert à expliquer, corriger, répondre aux questions — jamais à générer le code des exercices/projets à ma place. Mon quotidien pro est déjà 100 % orchestration ; la formation doit être 100 % construction.
- **Les evals sont prioritaires** : signal d'embauche n°1 senior vs mid, compétence la plus rare.
- **Structure de suivi** : `ROADMAP.md` = source de vérité (cases à cocher, 6 phases, semaine par semaine) ; livre *AI Engineering* de Chip Huyen = manuel transversal ; supports externes avec progression intégrée (Exercism, DeepLearning.AI, HF Agents Course) ; journal quotidien dans `journal/`.
- Une milestone GitHub par phase ; revue et ajustement de la roadmap à chaque fin de phase.

## Comment m'aider dans ce repo

- Si je bloque sur un exercice : m'expliquer le concept, me donner des indices — pas la solution complète.
- Si je te montre mon code : review exigeante (idiomes Python, typing, tests), comme un senior le ferait.
- Lors des revues hebdo : m'aider à faire le bilan à partir du journal et à préparer les objectifs de la semaine suivante.
- Me challenger si je dérive vers du contenu passif ou hors roadmap.

## Mécanique des sessions (important)

- `ROADMAP.md` = vue macro (phases/semaines). `phases/phase-N-*/SESSIONS.md` = plan détaillé session par session de la phase en cours (objectif, tâches précises, critère "✅ fini quand"). Seule la phase en cours est détaillée ; le SESSIONS.md de la phase suivante est généré à la rétrospective de fin de phase, ajusté à la vitesse réelle.
- Skill `/session` (dans `.claude/skills/session/`) : sans argument = brief du jour (où j'en suis + quoi faire) ; `fin` = journal + `scripts/update_progress.py` (tableau de bord README) + `scripts/update_calendar.py` (calendrier) + commit/push, tout en automatique ; `revue` = revue hebdo.
- Calendrier : `calendar/formation.ics` est GÉNÉRÉ par `scripts/update_calendar.py` (ne pas l'éditer à la main) — un événement par jour avec le programme de la prochaine session non faite. Horaires : lun-ven 7h-8h, samedi 10h-12h. À consommer en abonnement par URL (raw GitHub), pas en import.

## État d'avancement

- Roadmap v1 + SESSIONS.md phase 1 (40 sessions détaillées) + skill /session rédigés, en attente de ma relecture. Pas encore commencé la phase 1.
- Reste à faire au setup : `git init`, création du repo GitHub public, éventuellement fichier .ics pour caler le créneau quotidien dans Google Calendar (créneau pas encore choisi).
