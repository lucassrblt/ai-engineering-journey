# AI Engineering Journey — Roadmap 12 mois

> Objectif : être capable de candidater sur des postes **AI Engineer / GenAI Engineer** dans 12 mois,
> avec un portfolio de 3 projets LLM déployés, testés par des evals, et documentés.
>
> Rythme : **5 sessions de 1h (lun-ven, 7h-8h) + samedi 2h (10h-12h : revue hebdo 45 min + session longue)**. Une semaine tampon toutes les ~6 semaines.
> Une "session" du plan peut déborder sur le lendemain : on reprend là où on s'est arrêté, le samedi sert de rattrapage.
> Règle d'or : pendant les sessions, **je tape le code moi-même**. L'IA sert à poser des questions, jamais à écrire à ma place.

## Fil rouge transversal

- 📖 **Manuel de cours** : [*AI Engineering* — Chip Huyen (O'Reilly, 2025)](https://github.com/chiphuyen/aie-book) — ~1 chapitre par quinzaine, en lecture hors sessions (transports, pauses).
- 📓 **Journal** : une entrée par session dans `journal/` (ce que j'ai appris, ce qui a bloqué, objectif de la prochaine session).
- ✅ **Avancement** : cocher les cases ici. Une milestone GitHub par phase.

---

> 🎯 **Quoi faire aujourd'hui, précisément ?** Chaque phase a son plan de sessions détaillé dans `phases/phase-N-*/SESSIONS.md`
> (objectif, tâches, critère "✅ fini quand" pour chaque session de 1h30). Le plan de la phase suivante est généré à la rétro de fin de phase.
> Encore plus simple : lancer `claude` dans ce dossier et taper `/session` — le brief du jour s'affiche tout seul.

## Phase 1 — Python par la pratique (semaines 1-8)

📋 Sessions détaillées : [`phases/phase-1-python/SESSIONS.md`](phases/phase-1-python/SESSIONS.md)

**Pourquoi** : le métier exige Python, et réécrire du code à la main reconstruit le muscle perdu.
**Support principal** : [Exercism — track Python](https://exercism.org/tracks/python) (progression intégrée + mentorat gratuit).
**Livrable de phase** : une API FastAPI complète, testée avec pytest, publiée sur ce repo.

- [ ] **S1** — Setup (uv, ruff, VS Code) + syntaxe de base. Exercism : "Learning mode" exercices 1-8. Comparer mentalement chaque concept à son équivalent JS/TS.
- [ ] **S2** — Structures de données (list, dict, set, tuple), slicing. Exercism 9-16. Mini-script : parser un CSV sans lib.
- [ ] **S3** — Comprehensions, générateurs, fonctions (args/kwargs, closures). Exercism 17-24.
- [ ] **S4** — Classes, dataclasses, typing (le `TypeScript` de Python). Exercism 25-32. Porter un petit service TS existant en Python.
- [ ] **S5** — Gestion d'erreurs, context managers, modules/packages, venv. Exercism 33-40.
- [ ] **S6** — pytest : fixtures, paramétrage, mocking. Écrire les tests des scripts des semaines 2-4.
- [ ] **S7** — FastAPI : routes, Pydantic, dépendances, async (comparer à Express/Nest). Démarrer le projet de phase : API REST (ex. gestionnaire de bookmarks) avec auth simple.
- [ ] **S8** — Finir le projet : tests, Dockerfile, README. 🏁 **Livrable publié.**
- 📖 Lecture : Chip Huyen ch. 1 (Introduction to Building AI Applications) + ch. 2 (Understanding Foundation Models).

## Phase 2 — Fondamentaux LLM (semaines 9-16)

**Pourquoi** : le cœur du métier — construire sur les API de modèles, pas entraîner des modèles.
**Supports** : docs & cookbook Anthropic, [DeepLearning.AI short courses](https://www.deeplearning.ai/courses/) (sélection ci-dessous).
**Livrable de phase** : un CLI d'analyse de documents publié (résumé, classification, extraction structurée).

- [ ] **S9** — Premier appel API (SDK Anthropic Python) : messages, rôles, system prompt, température, max_tokens. Comprendre la tokenisation et les coûts.
- [ ] **S10** — Streaming, gestion d'erreurs, retries, rate limits. Wrapper propre réutilisable.
- [ ] **S11** — Prompt engineering sérieux : few-shot, chain-of-thought, délimiteurs, prompts versionnés dans le code. Cours DLAI : *Prompt Engineering*.
- [ ] **S12** — Structured outputs & function calling : JSON garanti, validation Pydantic. Premier outil appelé par le modèle.
- [ ] **S13** — Semaine tampon / rattrapage. Si à jour : explorer un 2e provider (OpenAI) pour comparer les API.
- [ ] **S14** — Démarrer le CLI d'analyse de documents : ingestion (PDF/txt), résumé, classification.
- [ ] **S15** — CLI suite : extraction structurée, function calling, gestion des gros documents (découpage).
- [ ] **S16** — Finir : tests, suivi des coûts par run, README avec exemples. 🏁 **Livrable publié.**
- 📖 Lecture : Chip Huyen ch. 3 (Evaluation Methodology) + ch. 5 (Prompt Engineering).

## Phase 3 — RAG (semaines 17-24)

**Pourquoi** : le pattern LLM le plus déployé en production ; demandé dans quasi toutes les offres.
**Supports** : cours DLAI RAG + Chip Huyen ch. 6. Base vectorielle : **pgvector** (capitalise sur ma connaissance des BDD).
**Livrable de phase** : "Chat avec une documentation" déployé, avec citations des sources.

- [ ] **S17** — Embeddings : intuition, génération, similarité cosinus. Petit moteur de recherche sémantique en mémoire.
- [ ] **S18** — pgvector : setup Postgres, index, requêtes de similarité. Ingestion d'un vrai corpus.
- [ ] **S19** — Chunking : par taille, par paragraphe, par structure. Mesurer l'impact sur la qualité de retrieval.
- [ ] **S20** — Pipeline RAG complet : question → retrieval → prompt augmenté → réponse avec citations.
- [ ] **S21** — Les cas durs : question hors corpus (refuser de répondre), recherche hybride (vecteur + keyword), reranking.
- [ ] **S22** — Semaine tampon / rattrapage.
- [ ] **S23** — Interface (FastAPI + front simple ou Streamlit) + déploiement (Railway/Fly.io).
- [ ] **S24** — Finir : monitoring des coûts, README avec choix d'architecture justifiés. 🏁 **Livrable déployé.**
- 📖 Lecture : Chip Huyen ch. 6 (RAG & Agents — partie RAG).

## Phase 4 — Agents & MCP (semaines 25-32)

**Pourquoi** : orchestration d'agents + MCP = compétences n°1 des offres 2026. Mon expérience quotidienne d'orchestration devient un atout différenciant : je passe du côté constructeur.
**Supports** : [Hugging Face Agents Course](https://huggingface.co/learn/agents-course) + HF MCP Course + Claude Agent SDK.
**Livrable de phase** : un agent multi-étapes utile + mon propre serveur MCP publié.

- [ ] **S25** — HF Agents Course unités 1-2 : boucle agentique, tool use, ReAct. Implémenter une boucle agentique **à la main** (sans framework) pour comprendre.
- [ ] **S26** — Tool use avancé : définir de bons outils, gestion des erreurs d'outils, état de la conversation.
- [ ] **S27** — MCP : le protocole, puis écrire mon premier serveur MCP (ex. exposer une BDD ou une API métier).
- [ ] **S28** — Un framework : Claude Agent SDK ou LangGraph. Refaire l'agent de la S25 avec, comparer.
- [ ] **S29** — Semaine tampon / rattrapage.
- [ ] **S30** — Projet de phase : agent multi-étapes réel (ex. veille automatisée : recherche → synthèse → rapport ; ou triage d'emails/tickets).
- [ ] **S31** — Durcir : guardrails, limites de coûts, human-in-the-loop, timeouts.
- [ ] **S32** — Finir : README, démo vidéo courte. 🏁 **Livrables publiés (agent + serveur MCP).**
- 📖 Lecture : Chip Huyen ch. 6 (partie Agents) + ch. 10 (AI Engineering Architecture & User Feedback).

## Phase 5 — Evals & observabilité (semaines 33-40)

**Pourquoi** : LE signal senior en entretien ("sketch an eval pipeline" sépare les seniors des mids) et la compétence la plus rare du marché. Ma culture des tests E2E se transpose directement.
**Supports** : Chip Huyen ch. 3-4 (relecture appliquée), cours DLAI *Evaluating and Debugging*, [Langfuse](https://langfuse.com/) (open source).
**Livrable de phase** : suites d'evals + tracing ajoutés aux projets des phases 3 et 4.

- [ ] **S33** — Golden dataset : construire 50+ cas de test pour le projet RAG (questions, réponses attendues, cas pièges, hors-corpus).
- [ ] **S34** — Métriques RAG : précision du retrieval, faithfulness, pertinence. Scorer automatiquement.
- [ ] **S35** — LLM-as-judge : prompts de juge, biais connus, calibration contre jugement humain.
- [ ] **S36** — Suite de régression : CI GitHub Actions qui rejoue les evals à chaque changement de prompt/modèle.
- [ ] **S37** — Tracing avec Langfuse : instrumenter l'agent de la phase 4 (traces, coûts, latences par étape).
- [ ] **S38** — Evals d'agent : taux de réussite de tâche, détection de boucles, analyse des échecs.
- [ ] **S39** — Semaine tampon / rattrapage.
- [ ] **S40** — Rédiger un post technique : "Ce que j'ai appris en construisant des evals". 🏁 **Livrable : les 2 projets ont CI d'evals + tracing.**
- 📖 Lecture : Chip Huyen ch. 4 (Evaluate AI Systems) + ch. 9 (Inference Optimization — latence & coûts).

## Phase 6 — Projet phare & positionnement (semaines 41-48)

**Pourquoi** : consolider en un projet de niveau professionnel, et convertir le travail en opportunités.
**Livrable final** : un produit LLM complet en production + profil repositionné + candidatures lancées.

- [ ] **S41-42** — Choisir et cadrer le projet phare (combine RAG + agent + evals + observabilité ; idéalement lié à un vrai besoin, peut-être un livrable du master). Architecture documentée AVANT de coder.
- [ ] **S43-45** — Construire. Standards pro : tests, CI, Docker, déploiement, budget de coûts.
- [ ] **S46** — Culture ML express (pour les entretiens) : embeddings, fine-tuning, overfitting, quantization — comprendre, pas pratiquer. + Chip Huyen ch. 7-8 (Finetuning, Dataset Engineering) en lecture rapide.
- [ ] **S47** — CV + LinkedIn refaits autour des projets. Ce repo mis en avant. 2-3 posts techniques publiés.
- [ ] **S48** — Candidatures ciblées (AI Engineer, GenAI Engineer, Forward Deployed Engineer) + préparation entretiens : whiteboarder un pipeline d'evals, expliquer chaque choix d'architecture des projets. 🏁

---

## Gabarit d'une session (1h en semaine)

1. **5 min** — `/session` : brief du jour + rappel de la veille.
2. **45 min** — l'objectif du jour (une seule chose).
3. **10 min** — `/session fin` : journal, avancement, calendrier et commit automatiques.

Le samedi (2h) : `/session revue` (45 min) puis session longue (1h15) — mini-projet de la semaine ou rattrapage.

## Règles anti-décrochage

- Rater une session = zéro culpabilité, on reprend à la case non cochée. Le plan a des semaines tampons pour ça.
- Une session sans motivation = faire uniquement 30 min d'Exercism ou de lecture. Le rendez-vous compte plus que le contenu.
- Fin de chaque phase = **revue de la roadmap** : ajuster les phases suivantes à ma vitesse réelle (ce fichier est un contrat révisable, pas un dogme).
- Jamais de tutoriel passif pendant les sessions : si je regarde une vidéo, c'est notebook ouvert.
