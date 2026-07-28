---
name: session
description: Démarrer ou clôturer une session de formation - dit exactement quoi faire aujourd'hui
argument-hint: [fin]
---

# Session de formation

## Si l'argument est vide ou "start" → DÉMARRAGE de session

1. Lire la dernière entrée de `journal/` (fichier le plus récent) et le `SESSIONS.md` de la phase en cours (la première phase dont toutes les sessions ne sont pas encore faites, en croisant avec les entrées du journal).
2. Déterminer la session du jour : la première session de SESSIONS.md non couverte par une entrée de journal.
3. Afficher un brief de démarrage, court et actionnable :
   - **Où j'en suis** : semaine X, session Y, N sessions faites sur la phase.
   - **Rappel de la veille** : les 2-3 points clés de la dernière entrée de journal (rappel actif).
   - **Aujourd'hui** : l'objectif, les tâches précises (recopiées de SESSIONS.md avec les liens), le critère "✅ fini quand".
   - Si la dernière session date de plus de 3 jours : le dire sans culpabiliser et proposer 10 min de révision en plus du programme.
4. Ne PAS générer le code des exercices. Pendant la session, répondre aux questions, expliquer les concepts, donner des indices — la règle du repo (CLAUDE.md) : Lucas tape lui-même.

## Si l'argument est "fin" → CLÔTURE de session

1. Demander (ou déduire de la conversation si la session s'est faite ici) : ce qui a été fait, ce qui a bloqué, ce qui a été appris.
2. Créer l'entrée de journal `journal/AAAA-MM-JJ.md` à partir de `journal/TEMPLATE.md`, en remplissant :
   - les acquis et blocages,
   - **l'objectif de la prochaine session** (lu depuis SESSIONS.md — c'est ce qui rend le prochain démarrage sans friction).
3. Si la session termine une semaine : cocher la case correspondante dans `ROADMAP.md`.
4. Si un blocage est récurrent (apparu dans ≥2 entrées) : le signaler et proposer d'adapter la prochaine session.
5. Mettre à jour automatiquement (sans demander) :
   - `python3 scripts/update_progress.py` — tableau de bord du README ;
   - `python3 scripts/update_calendar.py` — régénère le calendrier avec les prochaines sessions.
6. Commit + push automatiques (sans demander) : `git add -A && git commit -m "journal: SX.Y - <résumé court>" && git push` (ne pas push si aucun remote configuré). Inclure le travail de la session s'il est dans ce repo.

## Si l'argument est "revue" → REVUE HEBDOMADAIRE (45 min)

1. Lire toutes les entrées de journal de la semaine.
2. Bilan : sessions faites/prévues, vitesse réelle vs plan, blocages récurrents, points de fierté.
3. Cocher la semaine dans ROADMAP.md si complète ; sinon, proposer le report (les semaines tampons servent à ça).
4. Mettre à jour automatiquement : `python3 scripts/update_progress.py` et `python3 scripts/update_calendar.py`, puis commit + push.
5. Afficher l'objectif de la semaine suivante et vérifier que les prérequis sont prêts (comptes, installs).
