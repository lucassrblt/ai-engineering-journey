# Phase 1 — Python par la pratique · Plan de sessions détaillé

> 8 semaines × 5 sessions de 1h30. Chaque session : **Objectif → Tâches → ✅ Fini quand**.
> Prérequis unique (à faire avant la S1.1, ~20 min) : créer un compte [Exercism](https://exercism.org/tracks/python) et rejoindre le track Python en mode "Learning".

## Semaine 1 — Setup & syntaxe de base

### S1.1 — Environnement de travail
- Installer [uv](https://docs.astral.sh/uv/) (`curl -LsSf https://astral.sh/uv/install.sh | sh`), puis `uv python install 3.12`.
- VS Code : extensions Python + Ruff. Créer `~/Desktop/dev/ai-engineering-journey/phases/phase-1-python/playground/` avec `uv init`.
- Écrire un premier script `hello.py` : lire son prénom en argument CLI (`sys.argv`), afficher un message. Le lancer avec `uv run`.
- Configurer Exercism CLI (`exercism configure`) pour faire les exos en local.
- ✅ Fini quand : `uv run hello.py Lucas` fonctionne + un exo Exercism soumis depuis le terminal.

### S1.2 — Variables, nombres, strings
- Exercism : *Hello World*, *Guido's Gorgeous Lasagna* (basics), *Currency Exchange* (numbers).
- Dans le playground : porter en Python 5 one-liners que tu écrirais en JS (template literals → f-strings, `parseInt` → `int()`, etc.). Noter les différences dans le journal.
- ✅ Fini quand : 3 exos verts + fichier `js-vs-python.md` commencé avec ≥5 équivalences.

### S1.3 — Booléens, conditions, boucles
- Exercism : *Ghost Gobble Arcade Game* (bools), *Meltdown Mitigation* (conditionals), *Making the Grade* (loops).
- Piège à noter : truthiness Python vs JS (`[] == false` n'existe pas ici), `elif`, absence de `++`.
- ✅ Fini quand : 3 exos verts + section "conditions/boucles" ajoutée à `js-vs-python.md`.

### S1.4 — Strings en profondeur
- Exercism : *Little Sister's Vocabulary* (string methods), *Inventory Management* si dispo, sinon exo libre du track.
- Playground : écrire `slugify.py` (titre → slug URL) sans regex, puis avec le module `re`.
- ✅ Fini quand : exos verts + `slugify.py` gère accents, espaces multiples, ponctuation.

### S1.5 — Mini-projet de semaine + revue
- Écrire `stats_texte.py` : lit un fichier texte, affiche nombre de mots, top 10 des mots fréquents, longueur moyenne des phrases. Uniquement stdlib.
- Revue hebdo (45 min) : relire le journal de la semaine, cocher la S1 dans ROADMAP.md, lire l'objectif de la semaine 2.
- ✅ Fini quand : le script tourne sur un vrai fichier + commit + entrée de journal de revue.

## Semaine 2 — Structures de données

### S2.1 — Listes
- Exercism : *Card Games* (lists), *Chaitana's Colossal Coaster* (list methods).
- Piège : les listes sont mutables par référence (comme JS) mais le slicing copie — jouer avec `a = b[:]` vs `a = b`.
- ✅ Fini quand : 2 exos verts + démo slicing dans le playground (5 exemples commentés).

### S2.2 — Dictionnaires
- Exercism : *Inventory Management* (dicts), *Mecha Munch Management* (dict methods).
- Playground : porter un objet de config TS typique en dict Python ; tester `.get()` avec défaut, `setdefault`, itération `.items()`.
- ✅ Fini quand : 2 exos verts + comparaison `Map`/objet JS vs dict notée dans `js-vs-python.md`.

### S2.3 — Tuples & sets
- Exercism : *Tisbury Treasure Hunt* (tuples), *Cater Waiter* (sets).
- Comprendre : tuple = immuable + unpacking (`a, b = b, a`) ; set = unions/intersections (pense opérations SQL).
- ✅ Fini quand : 2 exos verts + un exemple concret d'usage de set (dédoublonnage d'emails).

### S2.4 — Parser un CSV sans lib
- Playground : `parse_csv.py` — lire un CSV (généré depuis un export quelconque), le parser en liste de dicts **sans** le module `csv`, gérer les champs entre guillemets.
- Puis refaire en 5 lignes avec `csv.DictReader` pour mesurer ce que la stdlib apporte.
- ✅ Fini quand : les deux versions donnent le même résultat sur un fichier de test.

### S2.5 — Mini-projet + revue
- `top_depenses.py` : à partir du CSV de la S2.4 (ex. dépenses), grouper par catégorie, sommer, trier, afficher un tableau. Structures pures, pas de pandas.
- Revue hebdo : journal, cocher S2, lire S3.
- ✅ Fini quand : sortie correcte vérifiée à la main + commit.

## Semaine 3 — Comprehensions, générateurs, fonctions

### S3.1 — List/dict comprehensions
- Exercism : exos du concept *comprehensions* du track.
- Playground : réécrire 5 boucles des semaines 1-2 en comprehensions. Règle : si ça ne tient pas en une ligne lisible, garder la boucle.
- ✅ Fini quand : exos verts + les 5 réécritures commitées avec avant/après en commentaire.

### S3.2 — Générateurs & lazy evaluation
- Exercism : concept *generators*.
- Playground : `lire_gros_fichier.py` — itérer un fichier de 100 Mo ligne à ligne avec un générateur (créer le fichier avec un script). Comparer la RAM avec une lecture complète (`ps` ou `resource`).
- ✅ Fini quand : tu sais expliquer par écrit (journal) quand `yield` vs liste.

### S3.3 — Fonctions : *args, **kwargs, valeurs par défaut
- Exercism : concept *function arguments* / *unpacking*.
- Piège classique à provoquer volontairement : le défaut mutable (`def f(x, acc=[])`) — le reproduire, comprendre, noter.
- ✅ Fini quand : exos verts + le piège du défaut mutable expliqué dans `js-vs-python.md`.

### S3.4 — Closures, lambdas, fonctions d'ordre supérieur
- Playground : recoder `debounce`-like et `memoize` en Python (tu les connais en JS). Puis découvrir `functools.lru_cache` et comparer.
- ✅ Fini quand : `memoize` maison passe un test simple + version `lru_cache` en 2 lignes.

### S3.5 — Mini-projet + revue
- `pipeline.py` : enchaîner lecture CSV → filtre → transformation → agrégation, en composant des générateurs (style pipeline de données).
- Revue hebdo : journal, cocher S3, lire S4.
- ✅ Fini quand : pipeline lisible, chaque étape testable indépendamment.

## Semaine 4 — Classes, dataclasses, typing

### S4.1 — Classes de base
- Exercism : concept *classes*.
- Playground : porter une classe TS simple (ex. `class User` avec méthodes) — comprendre `self`, `__init__`, `__repr__`.
- ✅ Fini quand : exos verts + équivalence classe TS/Python dans `js-vs-python.md`.

### S4.2 — Dataclasses
- Lire la doc `dataclasses`. Refaire la classe de S4.1 en dataclass ; ajouter `frozen=True`, valeurs par défaut, `field(default_factory=...)`.
- Comprendre : dataclass ≈ interface TS + constructeur gratuit.
- ✅ Fini quand : 3 dataclasses modélisant un petit domaine (User, Order, Product) avec relations.

### S4.3 — Typing
- Lire le [cheat sheet mypy](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html). Typer TOUT le code des semaines 1-3 : `list[str]`, `dict[str, int]`, `Optional`, `Union`, `Callable`, `TypedDict`.
- Lancer `uv run mypy playground/` et corriger jusqu'à zéro erreur.
- ✅ Fini quand : mypy passe sur tout le playground.

### S4.4-S4.5 — Projet : porter un service TS en Python (+ revue en fin de S4.5)
- Choisir un petit service TS que tu connais bien (~100-200 lignes : un service de validation, un client d'API, un utilitaire métier). Le porter en Python typé, avec dataclasses.
- Revue hebdo en fin de S4.5 : journal, cocher S4. **Point d'étape : si les semaines 1-4 ont été faciles, compresser les semaines 5-6 en une seule (le plan se révise).**
- ✅ Fini quand : le port fonctionne, mypy passe, README de 10 lignes expliquant les choix.

## Semaine 5 — Erreurs, contexte, modules

### S5.1 — Exceptions
- Exercism : concept *exceptions* (*Instrument tuning* ou équivalent).
- Différences vs JS : hiérarchie d'exceptions, `except SpecificError`, `else`/`finally`, `raise ... from e`.
- ✅ Fini quand : exos verts + le client d'API de S4 a une gestion d'erreurs propre (exceptions custom).

### S5.2 — Context managers
- Comprendre `with` (fichiers, locks). Écrire un context manager maison avec `@contextmanager` (ex. chronomètre de bloc de code).
- ✅ Fini quand : `with chrono("parsing"):` fonctionne et logge la durée.

### S5.3 — Modules & packages
- Restructurer le playground en vrai package : `src/`, `__init__.py`, imports absolus, `pyproject.toml` propre avec uv.
- Comprendre `if __name__ == "__main__":` et les entry points.
- ✅ Fini quand : `uv run python -m monpackage` fonctionne, imports propres partout.

### S5.4 — Stdlib tour
- Explorer en les utilisant : `pathlib` (vs `fs`), `json`, `datetime`, `collections` (Counter, defaultdict), `itertools` (islice, groupby).
- Refactorer `stats_texte.py` (S1.5) avec `Counter` et `pathlib`.
- ✅ Fini quand : le refactor divise le code par ~2.

### S5.5 — Mini-projet + revue
- `veille_hn.py` : script qui appelle l'API publique Hacker News (`httpx`), récupère le top 10, filtre par mots-clés, sauvegarde en JSON avec horodatage. Premier vrai script utile du parcours.
- Revue hebdo : journal, cocher S5, lire S6.
- ✅ Fini quand : le script tourne en cron-able (aucune interaction), erreurs réseau gérées.

## Semaine 6 — pytest

### S6.1 — Bases de pytest
- Installer pytest via uv. Lire [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html). Écrire les premiers tests de `slugify.py` et `parse_csv.py` : cas nominaux + cas limites.
- ✅ Fini quand : ≥10 tests verts, dont 3 cas limites que tu as trouvés toi-même.

### S6.2 — Fixtures & paramétrage
- `@pytest.fixture` (fichiers temporaires avec `tmp_path`), `@pytest.mark.parametrize` pour tester `slugify` sur 15 entrées en un seul test.
- ✅ Fini quand : les tests CSV utilisent une fixture `tmp_path`, slugify est paramétré.

### S6.3 — Mocking
- `monkeypatch` et `unittest.mock` : tester `veille_hn.py` SANS appel réseau réel (mocker httpx).
- Comparer mentalement à ce que tu connais (jest.mock).
- ✅ Fini quand : la suite passe en mode avion.

### S6.4 — Couverture & CI
- `pytest-cov` : mesurer, viser >80 % sur le playground. GitHub Actions : workflow qui lance ruff + mypy + pytest à chaque push (tu connais GHA, c'est du transfert direct).
- ✅ Fini quand : badge CI vert sur le repo.

### S6.5 — Kata + revue
- Kata de synthèse sans aide : implémenter en TDD une mini-bibliothèque `rate_limiter.py` (N appels max par fenêtre glissante). Tests d'abord.
- Revue hebdo : journal, cocher S6, lire le cadrage du projet de phase (S7).
- ✅ Fini quand : TDD respecté (historique de commits en témoigne), tests verts.

## Semaines 7-8 — Projet de phase : API FastAPI

> Projet : **API de gestion de bookmarks** (ou équivalent que tu préfères — décision à prendre en S7.1, pas après).
> Endpoints : CRUD bookmarks, tags, recherche, import/export JSON. Auth par token simple.

### S7.1 — Cadrage & squelette
- Lire [FastAPI First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/) (30 min max). Décider le périmètre exact (l'écrire dans un mini-README AVANT de coder).
- Squelette : uv + FastAPI + structure `src/` de la S5.3. Endpoint `/health`.
- ✅ Fini quand : `uvicorn` lance l'app, `/health` répond, structure commitée.

### S7.2 — Modèles & validation Pydantic
- Modèles Pydantic (c'est le Zod de Python) : Bookmark, Tag, requêtes/réponses séparées. Comparer à tes DTO Nest.
- ✅ Fini quand : POST /bookmarks valide et rejette proprement (422) les entrées invalides.

### S7.3 — CRUD complet
- Stockage : SQLite via `sqlite3` ou SQLModel (choix rapide, pas de débat d'archi — SQLite suffit).
- GET/POST/PUT/DELETE + pagination sur la liste.
- ✅ Fini quand : CRUD testable via la doc auto `/docs`.

### S7.4 — Dépendances & auth
- `Depends()` : injection de la DB, auth par header token (comparer aux guards Nest et middlewares Express).
- ✅ Fini quand : routes protégées, 401 propre sans token.

### S7.5 — Recherche & tags + revue
- Endpoint recherche (texte + filtre par tags), relation bookmark↔tags.
- Revue hebdo : journal, cocher S7.
- ✅ Fini quand : recherche fonctionnelle testée via /docs.

### S8.1-S8.2 — Tests
- Suite pytest complète avec `TestClient` FastAPI : nominal + erreurs + auth. Viser >80 % de couverture.
- ✅ Fini quand : CI verte avec la suite complète.

### S8.3 — Docker & qualité
- Dockerfile multi-stage (tu sais faire — l'exercice est de le faire en écosystème Python/uv), docker-compose pour le dev.
- ✅ Fini quand : `docker compose up` → API fonctionnelle.

### S8.4 — README & publication
- README pro : description, install, exemples curl, choix d'architecture justifiés, ce que tu referais autrement.
- ✅ Fini quand : le repo est montrable à un recruteur tel quel.

### S8.5 — Rétrospective de phase 🏁
- Relire tout le journal de la phase. Écrire une rétro : ce qui a marché, la vitesse réelle vs plan, niveau de confiance en Python (1-10).
- Avec Claude (`/session fin` puis discussion) : **générer le SESSIONS.md détaillé de la phase 2** en ajustant selon la rétro.
- ✅ Fini quand : phase 1 cochée dans ROADMAP.md, SESSIONS.md phase 2 créé, milestone GitHub fermée.

---

## Lectures hors sessions (fil rouge, ~20 min/jour dans les transports)
- Semaines 1-4 : Chip Huyen ch. 1 — *Introduction to Building AI Applications with Foundation Models*.
- Semaines 5-8 : Chip Huyen ch. 2 — *Understanding Foundation Models*.
