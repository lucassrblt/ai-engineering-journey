# Phase 1 — Python par la pratique · Plan de sessions détaillé

> **Format d'une session** : 📖 Théorie (~15 min) → 💻 Pratique (~40 min) → ✅ Fini quand → ➕ Si temps restant.
> Le cœur (📖+💻) est calibré sur ~55 min ; le ➕ remplit le reste du créneau (et absorbe un créneau de 1h30 si un jour tu allonges).
> **Jamais à court** : si tout est fini, demande à Claude un quiz de révision sur les concepts des 3 derniers jours (`/session` sait le faire).
>
> **Rôle de Claude Code pendant la session** : tuteur — il t'explique la théorie du jour avec tes analogies JS/TS, répond à tes questions, review ton code. Il n'écrit PAS le code des exercices.
>
> Prérequis unique (avant S1.1, ~20 min) : compte [Exercism](https://exercism.org/tracks/python) + rejoindre le track Python en mode "Learning".

---

## Semaine 1 — Setup & syntaxe de base

> **Pourquoi cette semaine** : on installe un environnement Python *moderne* (uv/ruff — l'équivalent de pnpm/eslint, pas le Python poussiéreux des tutos de 2015) et on câble la syntaxe de base sur ce que tu sais déjà en JS. Le but n'est pas d'apprendre à programmer — tu sais — mais de re-mapper tes réflexes.
> **Concepts clés** : interpréteur & REPL, uv, f-strings, typage dynamique fort (vs faible en JS), indentation significative.

### S1.1 — Environnement de travail
**Pourquoi** : un env propre dès le départ évite le chaos pip/venv qui dégoûte la moitié des débutants Python.
- 📖 Théorie (15 min) : lire l'intro d'[uv](https://docs.astral.sh/uv/getting-started/) (sections *Installation* et *Features*). Demander à Claude : "explique-moi le rapport entre uv, pip, venv et pyproject.toml, en comparant à npm/pnpm/package.json".
- 💻 Pratique (40 min) : installer uv (`curl -LsSf https://astral.sh/uv/install.sh | sh`) puis `uv python install 3.12`. VS Code : extensions Python + Ruff. Créer `phases/phase-1-python/playground/` avec `uv init`. Écrire `hello.py` : lire un prénom en argument CLI (`sys.argv`) et afficher un message ; lancer avec `uv run hello.py Lucas`. Configurer Exercism CLI (`exercism configure`).
- ✅ Fini quand : `uv run hello.py Lucas` fonctionne + un exo Exercism soumis depuis le terminal.
- ➕ Si temps restant : explorer le REPL (`uv run python`) 10 min — c'est l'outil d'expérimentation n°1 en Python, il n'y a pas d'équivalent aussi central en JS.

### S1.2 — Variables, nombres, strings
**Pourquoi** : 80 % du code que tu écriras manipule des strings et des nombres ; les f-strings sont partout dans le code LLM (construction de prompts).
- 📖 Théorie (15 min) : [Exercism — concept Basics](https://exercism.org/tracks/python/concepts/basics) et [concept Numbers](https://exercism.org/tracks/python/concepts/numbers). Noter : `/` renvoie toujours un float, `//` est la division entière (pas de `Math.floor` nécessaire).
- 💻 Pratique (40 min) : Exercism *Hello World*, *Guido's Gorgeous Lasagna*, *Currency Exchange*. Puis dans le playground : porter 5 one-liners JS en Python (template literals → f-strings, `parseInt` → `int()`, `toFixed` → f-string `:.2f`…). Créer `js-vs-python.md` et y noter les équivalences.
- ✅ Fini quand : 3 exos verts + `js-vs-python.md` commencé avec ≥5 équivalences.
- ➕ Si temps restant : les méthodes de string dans le REPL (`.strip()`, `.split()`, `.join()` — attention, `join` est inversé par rapport à JS : `", ".join(liste)`).

### S1.3 — Booléens, conditions, boucles
**Pourquoi** : c'est là que les habitudes JS piègent le plus (truthiness différente, pas de `===`, pas de `++`).
- 📖 Théorie (15 min) : [Exercism — Bools](https://exercism.org/tracks/python/concepts/bools) et [Conditionals](https://exercism.org/tracks/python/concepts/conditionals). Demander à Claude : "les 5 pièges de truthiness Python pour un dev JS" (ex. `[] == False` est `False` ici, `0 == False` est `True`…).
- 💻 Pratique (40 min) : Exercism *Ghost Gobble Arcade Game*, *Meltdown Mitigation*, *Making the Grade*. Attention à `elif`, `range()`, et `for...in` qui itère les *valeurs* (pas les clés comme en JS).
- ✅ Fini quand : 3 exos verts + section "conditions/boucles" dans `js-vs-python.md`.
- ➕ Si temps restant : `enumerate()` et `zip()` — les deux idiomes de boucle que tu utiliseras tous les jours (équivalents de `entries()` et d'un zip lodash).

### S1.4 — Strings en profondeur
**Pourquoi** : le text processing est LE quotidien de l'AI engineering (nettoyer des documents, parser des sorties de LLM).
- 📖 Théorie (15 min) : [Exercism — String methods](https://exercism.org/tracks/python/concepts/string-methods) + survoler la [doc du module `re`](https://docs.python.org/3/library/re.html) (juste `search`, `sub`, `findall`).
- 💻 Pratique (40 min) : Exercism *Little Sister's Vocabulary* + un exo string libre du track. Puis écrire `slugify.py` (titre → slug URL) d'abord SANS regex, puis avec `re.sub`.
- ✅ Fini quand : exos verts + `slugify.py` gère accents (`unicodedata.normalize`), espaces multiples, ponctuation.
- ➕ Si temps restant : demander à Claude 5 cas limites vicieux pour `slugify` et les faire passer.

### S1.5 — Mini-projet de semaine
**Pourquoi** : première synthèse sans guide — c'est l'effort de rappel qui ancre la semaine.
- 📖 Théorie (10 min) : relire `js-vs-python.md` en entier (c'est TON cours, écrit par toi).
- 💻 Pratique (45 min) : `stats_texte.py` — lit un fichier texte, affiche nombre de mots, top 10 des mots fréquents, longueur moyenne des phrases. Stdlib uniquement, sans regarder les sessions précédentes (y revenir seulement si bloqué).
- ✅ Fini quand : le script tourne sur un vrai fichier + commit.
- ➕ Si temps restant : demander à Claude une review sévère du script (idiomes, nommage) et appliquer ses remarques.

---

## Semaine 2 — Structures de données

> **Pourquoi cette semaine** : listes et dicts sont les structures que tu manipuleras dans TOUT le code LLM (messages = liste de dicts, réponses API = dicts imbriqués, chunks = listes). La maîtrise fine (slicing, méthodes, mutabilité) fait la différence entre du Python subi et du Python fluide.
> **Concepts clés** : mutabilité & références, slicing, dict comme structure universelle, tuple = immuable, set = opérations ensemblistes.

### S2.1 — Listes
**Pourquoi** : l'équivalent des arrays JS, mais avec le slicing en plus — l'idiome le plus utilisé du langage.
- 📖 Théorie (15 min) : [Exercism — Lists](https://exercism.org/tracks/python/concepts/lists) + [List methods](https://exercism.org/tracks/python/concepts/list-methods). Comprendre : `a = b` partage la référence (comme JS), `a = b[:]` copie.
- 💻 Pratique (40 min) : Exercism *Card Games*, *Chaitana's Colossal Coaster*. Playground : 5 exemples de slicing commentés (`lst[2:5]`, `lst[-3:]`, `lst[::2]`, `lst[::-1]`, copie).
- ✅ Fini quand : 2 exos verts + démo slicing commitée.
- ➕ Si temps restant : `sort()` vs `sorted()` et le paramètre `key=` (ton `Array.sort(fn)` en mieux).

### S2.2 — Dictionnaires
**Pourquoi** : les réponses des API LLM sont des dicts imbriqués ; tu vivras dedans.
- 📖 Théorie (15 min) : [Exercism — Dicts](https://exercism.org/tracks/python/concepts/dicts) + [Dict methods](https://exercism.org/tracks/python/concepts/dict-methods). Différence clé avec les objets JS : accès par `d["clé"]` qui lève `KeyError`, d'où `.get(clé, défaut)`.
- 💻 Pratique (40 min) : Exercism *Inventory Management*, *Mecha Munch Management*. Playground : porter un objet de config TS en dict ; utiliser `.get()`, `setdefault`, itération `.items()`.
- ✅ Fini quand : 2 exos verts + comparaison `Map`/objet JS vs dict dans `js-vs-python.md`.
- ➕ Si temps restant : dicts imbriqués — écrire une fonction `get_path(d, "a.b.c")` (ton `lodash.get`).

### S2.3 — Tuples & sets
**Pourquoi** : pas de vrai équivalent JS courant — ce sont les deux structures qui font gagner du code (unpacking, dédoublonnage, intersections).
- 📖 Théorie (15 min) : [Exercism — Tuples](https://exercism.org/tracks/python/concepts/tuples) + [Sets](https://exercism.org/tracks/python/concepts/sets). L'unpacking (`a, b = b, a`) et les opérateurs de sets (`&`, `|`, `-`) — pense opérations SQL.
- 💻 Pratique (40 min) : Exercism *Tisbury Treasure Hunt*, *Cater Waiter*. Playground : dédoublonner une liste d'emails en préservant l'ordre (set + astuce), intersection de deux listes de tags.
- ✅ Fini quand : 2 exos verts + les deux exemples commités.
- ➕ Si temps restant : `collections.Counter` en avant-première (compte les occurrences en 1 ligne — refactorera `stats_texte.py` en S5.4).

### S2.4 — Parser un CSV sans lib
**Pourquoi** : exercice de synthèse strings + listes + dicts, et leçon sur la valeur de la stdlib.
- 📖 Théorie (10 min) : survoler la doc du [module `csv`](https://docs.python.org/3/library/csv.html) (`DictReader`) — mais ne pas l'utiliser tout de suite.
- 💻 Pratique (45 min) : `parse_csv.py` — parser un CSV en liste de dicts À LA MAIN, y compris les champs entre guillemets contenant des virgules. Puis refaire en 5 lignes avec `csv.DictReader` et comparer.
- ✅ Fini quand : les deux versions donnent le même résultat sur un fichier de test.
- ➕ Si temps restant : gérer un cas tordu de plus (guillemets échappés `""`), ou demander un quiz de mi-semaine à Claude.

### S2.5 — Mini-projet de semaine
**Pourquoi** : grouper/sommer/trier des données = le cœur de tout traitement, et la base de ce que pandas automatise (que tu comprendras d'autant mieux).
- 📖 Théorie (10 min) : relire les sections de la semaine dans `js-vs-python.md` ; demander à Claude un mini-quiz (5 questions) sur listes/dicts/sets.
- 💻 Pratique (45 min) : `top_depenses.py` — depuis le CSV de S2.4 : grouper par catégorie, sommer, trier, afficher un tableau aligné (f-strings avec padding `:>10`).
- ✅ Fini quand : sortie correcte vérifiée à la main + commit.
- ➕ Si temps restant : ajouter un argument CLI `--mois` qui filtre.

---

## Semaine 3 — Comprehensions, générateurs, fonctions

> **Pourquoi cette semaine** : c'est la semaine qui transforme ton Python "traduit du JS" en Python idiomatique. Les comprehensions remplacent 80 % de tes `map`/`filter` ; les générateurs sont LE pattern pour traiter des gros corpus sans exploser la RAM (directement utile en RAG, phase 3).
> **Concepts clés** : comprehension, lazy evaluation, `yield`, `*args/**kwargs`, closures, le piège du défaut mutable.

### S3.1 — List/dict comprehensions
**Pourquoi** : l'idiome n°1 du langage — un code review Python juge d'abord ça.
- 📖 Théorie (15 min) : [Exercism — List comprehensions](https://exercism.org/tracks/python/concepts/list-comprehensions). Règle de lisibilité : une comprehension qui ne tient pas en une ligne lisible doit redevenir une boucle.
- 💻 Pratique (40 min) : exos du concept sur Exercism. Puis réécrire 5 boucles des semaines 1-2 en comprehensions (garder l'avant/après en commentaire).
- ✅ Fini quand : exos verts + les 5 réécritures commitées.
- ➕ Si temps restant : dict et set comprehensions (`{k: v for ...}`), comprehension avec condition double.

### S3.2 — Générateurs & lazy evaluation
**Pourquoi** : traiter un fichier de 10 Go ligne à ligne sans le charger — c'est exactement ce que fait un pipeline d'ingestion de documents.
- 📖 Théorie (15 min) : [Exercism — Generators](https://exercism.org/tracks/python/concepts/generators). Demander à Claude : "explique yield à quelqu'un qui connaît les async iterators JS".
- 💻 Pratique (40 min) : générer un fichier de ~100 Mo par script, puis comparer lecture complète vs générateur (mesurer la RAM avec `resource.getrusage`). Écrire un générateur `lire_par_blocs(path, n)`.
- ✅ Fini quand : tu sais expliquer par écrit dans le journal quand `yield` vs liste.
- ➕ Si temps restant : les generator expressions (`sum(x**2 for x in ...)`) et `itertools.islice`.

### S3.3 — Fonctions : *args, **kwargs, défauts
**Pourquoi** : toutes les signatures des SDK (Anthropic inclus) utilisent des kwargs — il faut les lire couramment.
- 📖 Théorie (15 min) : [Exercism — Function arguments](https://exercism.org/tracks/python/concepts/function-arguments) + [Unpacking](https://exercism.org/tracks/python/concepts/unpacking-and-multiple-assignment).
- 💻 Pratique (40 min) : exos du concept. Puis provoquer volontairement le piège du défaut mutable (`def f(x, acc=[])`), observer, comprendre, noter dans `js-vs-python.md`.
- ✅ Fini quand : exos verts + le piège expliqué par écrit avec la solution (`acc=None`).
- ➕ Si temps restant : keyword-only arguments (`def f(*, model, temperature)`) — le style des SDK modernes.

### S3.4 — Closures & fonctions d'ordre supérieur
**Pourquoi** : tu les connais en JS — l'objectif est le transfert direct + découvrir `functools`.
- 📖 Théorie (10 min) : doc de [`functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache) ; demander à Claude la différence closure JS vs Python (`nonlocal`).
- 💻 Pratique (45 min) : recoder `memoize` en Python pur (tu l'as déjà fait en JS), puis le remplacer par `@lru_cache` — premier contact avec les décorateurs, qu'on ne théorise pas encore.
- ✅ Fini quand : `memoize` maison passe un test simple + version `lru_cache` fonctionne.
- ➕ Si temps restant : écrire un décorateur `@chrono` qui logge la durée d'une fonction (tu en auras besoin réellement pour mesurer les appels LLM).

### S3.5 — Mini-projet de semaine
**Pourquoi** : composer des générateurs = l'architecture de tout pipeline de données (et le pattern des frameworks d'ingestion RAG).
- 📖 Théorie (10 min) : quiz Claude sur la semaine (comprehensions, yield, kwargs).
- 💻 Pratique (45 min) : `pipeline.py` — lecture CSV → filtre → transformation → agrégation, chaque étape étant un générateur qui consomme le précédent.
- ✅ Fini quand : pipeline lisible, chaque étape testable indépendamment.
- ➕ Si temps restant : mesurer avec `@chrono` (S3.4) le coût de chaque étape.

---

## Semaine 4 — Classes, dataclasses, typing

> **Pourquoi cette semaine** : le typing Python est ton pont depuis TypeScript — c'est la semaine où tu vas te sentir chez toi. Les dataclasses préfigurent Pydantic (phase 2), la brique de validation de TOUT l'écosystème LLM (structured outputs = modèles Pydantic).
> **Concepts clés** : `self`, dunder methods, dataclasses, type hints, mypy.

### S4.1 — Classes de base
**Pourquoi** : comprendre `self` et `__init__` suffit pour lire 95 % du code orienté objet Python.
- 📖 Théorie (15 min) : [Exercism — Classes](https://exercism.org/tracks/python/concepts/classes). Les dunder methods : `__init__`, `__repr__`, `__eq__` (demander à Claude le mapping avec constructor/toString/equals).
- 💻 Pratique (40 min) : exos du concept + porter une classe TS simple (ex. `class User` avec méthodes) en Python.
- ✅ Fini quand : exos verts + équivalence classe TS/Python dans `js-vs-python.md`.
- ➕ Si temps restant : propriétés (`@property`) — les getters sans parenthèses.

### S4.2 — Dataclasses
**Pourquoi** : dataclass ≈ interface TS + constructeur gratuit ; c'est le modèle mental de Pydantic.
- 📖 Théorie (15 min) : [doc `dataclasses`](https://docs.python.org/3/library/dataclasses.html) (jusqu'à `field()`).
- 💻 Pratique (40 min) : refaire la classe de S4.1 en dataclass ; ajouter `frozen=True`, défauts, `field(default_factory=list)` (tiens, le piège de S3.3 revient). Modéliser un petit domaine : User, Order, Product avec relations.
- ✅ Fini quand : les 3 dataclasses + un script qui les instancie et les affiche.
- ➕ Si temps restant : `asdict()`, comparaison auto (`==`), tri par `sort_index`.

### S4.3 — Typing
**Pourquoi** : c'est TypeScript en annotations — et mypy est ton filet de sécurité pour tout le reste du parcours.
- 📖 Théorie (15 min) : [cheat sheet mypy](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) en entier (c'est court).
- 💻 Pratique (40 min) : typer TOUT le playground des semaines 1-3 : `list[str]`, `dict[str, int]`, `X | None`, `Callable`, `TypedDict`. Lancer `uv run mypy .` et corriger jusqu'à zéro erreur.
- ✅ Fini quand : mypy passe sur tout le playground.
- ➕ Si temps restant : `Protocol` (le structural typing, exactement les interfaces TS) — demander une démo à Claude et la recoder.

### S4.4 & S4.5 — Projet : porter un service TS en Python
**Pourquoi** : le test de réalité de la phase — si tu portes ~150 lignes de TS que tu connais en Python idiomatique typé, le langage est acquis.
- 📖 Théorie (10 min, S4.4) : choisir le service TS (~100-200 lignes : validation, client d'API, utilitaire métier) et le relire.
- 💻 Pratique (S4.4 + S4.5) : le porter en Python typé avec dataclasses. mypy zéro erreur.
- ✅ Fini quand : le port fonctionne + README de 10 lignes sur les choix (quoi traduire littéralement, quoi ré-idiomatiser).
- ➕ Si temps restant (S4.5) : **point d'étape** — si les semaines 1-4 ont été faciles, décider avec Claude de compresser les semaines 5-6 en une seule (le plan se révise).

---

## Semaine 5 — Erreurs, contexte, modules

> **Pourquoi cette semaine** : la gestion d'erreurs Python (hiérarchie d'exceptions, `with`) est très différente du try/catch JS, et c'est ce qui rend un client d'API robuste — compétence directement critique quand on appelle des LLM (timeouts, rate limits, erreurs 529).
> **Concepts clés** : hiérarchie d'exceptions, `raise from`, context managers, packages & imports, la stdlib qui remplace lodash.

### S5.1 — Exceptions
**Pourquoi** : `except Exception` attrape-tout est le bug n°1 des débutants ; la hiérarchie d'exceptions est la façon Python de faire du contrôle de flux d'erreur propre.
- 📖 Théorie (15 min) : [tutoriel officiel — Errors](https://docs.python.org/3/tutorial/errors.html) (sections 8.3 à 8.7) : `except SpecificError`, `else`, `finally`, `raise ... from e`.
- 💻 Pratique (40 min) : Exercism concept exceptions. Puis créer des exceptions custom (`class ApiError(Exception)`) et les utiliser dans le client de S4.
- ✅ Fini quand : exos verts + le client gère 3 types d'erreurs distincts proprement.
- ➕ Si temps restant : `try/except/else` vs le pattern early-return — demander à Claude quand préférer quoi.

### S5.2 — Context managers
**Pourquoi** : `with` est partout (fichiers, connexions, locks) et tu en écriras pour instrumenter des appels LLM.
- 📖 Théorie (15 min) : doc [`contextlib`](https://docs.python.org/3/library/contextlib.html) (`@contextmanager` seulement). Comprendre : c'est un try/finally emballé.
- 💻 Pratique (40 min) : écrire `chrono` en context manager (`with chrono("parsing"):` logge la durée) — oui, c'est le décorateur de S3.4 sous une autre forme : comprendre pourquoi les deux existent.
- ✅ Fini quand : les deux formes (`@chrono` et `with chrono(...)`) coexistent et marchent.
- ➕ Si temps restant : `tempfile.TemporaryDirectory` et `contextlib.suppress` — deux outils de test très utiles.

### S5.3 — Modules & packages
**Pourquoi** : la douleur classique du débutant Python, réglée une fois pour toutes — indispensable avant FastAPI.
- 📖 Théorie (15 min) : demander à Claude un cours express "imports Python pour dev Node : `__init__.py`, imports absolus vs relatifs, `python -m`, en comparant à ESM/CommonJS".
- 💻 Pratique (40 min) : restructurer le playground en vrai package `src/`, imports absolus, `pyproject.toml` propre. Faire fonctionner `uv run python -m monpackage`.
- ✅ Fini quand : structure propre, plus aucun import relatif hasardeux.
- ➕ Si temps restant : les entry points (`[project.scripts]` dans pyproject.toml) — transformer un script en commande installable.

### S5.4 — Tour de la stdlib
**Pourquoi** : la stdlib Python remplace lodash + date-fns + une partie de npm ; la connaître évite de réinventer.
- 📖 Théorie (15 min) : survoler [`pathlib`](https://docs.python.org/3/library/pathlib.html), [`collections`](https://docs.python.org/3/library/collections.html) (Counter, defaultdict), `itertools` (islice, groupby, chain).
- 💻 Pratique (40 min) : refactorer `stats_texte.py` (S1.5) avec `Counter` et `pathlib` — objectif : diviser le code par ~2.
- ✅ Fini quand : le refactor est commité avec l'avant/après.
- ➕ Si temps restant : `json` et `datetime` (timezones !) — 10 min chacun dans le REPL.

### S5.5 — Mini-projet de semaine
**Pourquoi** : premier script qui parle au réseau — la moitié du chemin vers un client LLM.
- 📖 Théorie (10 min) : quickstart de [httpx](https://www.python-httpx.org/quickstart/) (le fetch/axios de Python).
- 💻 Pratique (45 min) : `veille_hn.py` — API publique Hacker News, top 10, filtre par mots-clés, sauvegarde JSON horodatée. Erreurs réseau gérées avec les exceptions de S5.1.
- ✅ Fini quand : tourne sans interaction (cron-able), gère la panne réseau proprement.
- ➕ Si temps restant : ajouter un retry avec backoff exponentiel (3 tentatives) — pattern que tu réutiliseras tel quel pour les API LLM.

---

## Semaine 6 — pytest

> **Pourquoi cette semaine** : pytest est l'outil que tu utiliseras pour les evals en phase 5 — les suites d'evals LLM SONT des suites pytest. Ta culture de test E2E se transpose ici, avec des idiomes différents de Jest.
> **Concepts clés** : assertions nues, fixtures (l'injection de dépendances de pytest), paramétrage, mocking, couverture.

### S6.1 — Bases de pytest
**Pourquoi** : contrairement à Jest, pytest n'a ni `describe` ni `expect` — juste des fonctions et `assert` ; il faut recâbler les réflexes.
- 📖 Théorie (15 min) : [pytest — Getting started](https://docs.pytest.org/en/stable/getting-started.html) + demander à Claude un tableau Jest → pytest (describe/it/expect/beforeEach → fonctions/assert/fixtures).
- 💻 Pratique (40 min) : tester `slugify.py` et `parse_csv.py` : cas nominaux + cas limites trouvés par toi.
- ✅ Fini quand : ≥10 tests verts dont 3 cas limites.
- ➕ Si temps restant : `pytest -k`, `-x`, `--lf` — le workflow de debug rapide.

### S6.2 — Fixtures & paramétrage
**Pourquoi** : les fixtures sont LA différence conceptuelle avec Jest, et `parametrize` est l'outil des golden datasets d'evals (phase 5 — un eval = un test paramétré sur un dataset).
- 📖 Théorie (15 min) : [doc fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) (début) + [parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html).
- 💻 Pratique (40 min) : fixture `tmp_path` pour les tests CSV ; paramétrer `slugify` sur 15 entrées en un test.
- ✅ Fini quand : la suite utilise fixtures + parametrize, tout est vert.
- ➕ Si temps restant : une fixture à scope `module` (ex. dataset chargé une fois).

### S6.3 — Mocking
**Pourquoi** : tester du code qui appelle une API sans l'appeler — exactement ce qu'il faudra faire avec les LLM (on ne paie pas un appel Claude par test unitaire).
- 📖 Théorie (15 min) : `monkeypatch` ([doc](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)) vs `unittest.mock` — demander à Claude quand utiliser lequel (équivalents de jest.mock/spyOn).
- 💻 Pratique (40 min) : tester `veille_hn.py` sans réseau (mocker httpx), y compris le cas "l'API renvoie une 500".
- ✅ Fini quand : la suite passe en mode avion.
- ➕ Si temps restant : `respx` (mock httpx dédié) — comparer avec l'approche manuelle.

### S6.4 — Couverture & CI
**Pourquoi** : transfert direct de tes acquis GitHub Actions — le but est de voir que l'écosystème Python s'intègre pareil.
- 📖 Théorie (10 min) : doc `pytest-cov` (README suffit).
- 💻 Pratique (45 min) : mesurer la couverture, viser >80 % ; workflow GitHub Actions ruff + mypy + pytest sur push.
- ✅ Fini quand : badge CI vert sur le repo.
- ➕ Si temps restant : pre-commit hook local (ruff au commit).

### S6.5 — Kata TDD de synthèse
**Pourquoi** : dernière vérification avant le projet final — code sous contrainte, sans aide, tests d'abord.
- 📖 Théorie (5 min) : relire le cycle TDD (red → green → refactor).
- 💻 Pratique (50 min) : `rate_limiter.py` en TDD strict — N appels max par fenêtre glissante. (Ce n'est pas un hasard : les rate limiters sont un vrai sujet des clients LLM.)
- ✅ Fini quand : TDD visible dans l'historique de commits, tests verts.
- ➕ Si temps restant : variante token bucket, ou quiz de révision semaine 5-6.

---

## Semaines 7-8 — Projet de phase : API FastAPI

> **Pourquoi ce projet** : FastAPI est LE framework des services LLM en production (c'est lui qui servira tes projets RAG et agents des phases 3-4). Tout ce que tu as appris converge ici : typing (les routes sont typées), Pydantic (validation), pytest (la suite), packaging, Docker.
> **Projet : API de gestion de bookmarks** — CRUD, tags, recherche, auth token. (Remplaçable par un équivalent qui te motive plus — décision en S7.1, pas après.)

### S7.1 — Cadrage & squelette
- 📖 Théorie (20 min) : [FastAPI — First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/) + [Path params](https://fastapi.tiangolo.com/tutorial/path-params/). Noter la parenté avec Nest (décorateurs, DI).
- 💻 Pratique (35 min) : écrire le périmètre exact dans un mini-README AVANT de coder. Squelette uv + FastAPI + structure `src/` (S5.3). Endpoint `/health`.
- ✅ Fini quand : `uvicorn` sert `/health`, structure commitée.
- ➕ Si temps restant : explorer `/docs` (Swagger auto) — comprendre d'où il sort (des types !).

### S7.2 — Modèles Pydantic
- 📖 Théorie (15 min) : [Pydantic — Models](https://docs.pydantic.dev/latest/concepts/models/) (début). C'est le Zod de Python — et le moteur des structured outputs LLM en phase 2 : ce que tu apprends là est la brique la plus réutilisée du parcours.
- 💻 Pratique (40 min) : modèles Bookmark/Tag, schémas requête/réponse séparés (comme tes DTO Nest). POST /bookmarks qui valide et rejette en 422.
- ✅ Fini quand : la validation rejette proprement 3 payloads invalides différents.
- ➕ Si temps restant : validators custom (`@field_validator`) — valider une URL.

### S7.3 — CRUD complet
- 📖 Théorie (10 min) : survol [SQLModel](https://sqlmodel.tiangolo.com/) OU choix assumé du `sqlite3` brut — 5 min de réflexion, pas de débat d'archi, SQLite suffit.
- 💻 Pratique (45 min) : GET/POST/PUT/DELETE + pagination.
- ✅ Fini quand : CRUD complet testable via `/docs`.
- ➕ Si temps restant : tri et filtres sur la liste.

### S7.4 — Dépendances & auth
- 📖 Théorie (15 min) : [FastAPI — Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/). `Depends()` = l'injection de dépendances de Nest, en plus simple.
- 💻 Pratique (40 min) : injecter la DB par dépendance ; auth par header token ; 401 propre.
- ✅ Fini quand : routes protégées, testées à la main via /docs.
- ➕ Si temps restant : dépendance `get_current_user` chaînée (dépendance de dépendance).

### S7.5 — Recherche & tags
- 📖 Théorie (5 min) : rien de neuf — relire son propre code de la semaine (ça compte).
- 💻 Pratique (50 min) : endpoint recherche (texte + filtre tags), relation bookmark↔tags.
- ✅ Fini quand : recherche fonctionnelle via /docs.
- ➕ Si temps restant : ranking simple des résultats (occurrences dans le titre > description).

### S8.1 & S8.2 — Suite de tests
- 📖 Théorie (15 min, S8.1) : [FastAPI — Testing](https://fastapi.tiangolo.com/tutorial/testing/) (`TestClient`).
- 💻 Pratique : suite complète — nominal, erreurs, auth, pagination. Viser >80 % de couverture. CI verte.
- ✅ Fini quand : CI verte avec la suite complète.
- ➕ Si temps restant (S8.2) : un test de charge artisanal (boucle de 1000 requêtes chronométrée).

### S8.3 — Docker & qualité
- 📖 Théorie (10 min) : chercher "uv docker best practices" (doc officielle uv) — le multi-stage avec uv a ses subtilités.
- 💻 Pratique (45 min) : Dockerfile multi-stage + docker-compose dev. Tu sais faire — l'exercice est l'écosystème Python.
- ✅ Fini quand : `docker compose up` → API fonctionnelle.
- ➕ Si temps restant : image finale < 200 Mo (slim, pas de dev deps).

### S8.4 — README & publication
- 📖 Théorie (10 min) : relire 2 README de projets Python populaires pour calibrer.
- 💻 Pratique (45 min) : README pro — description, install, exemples curl, choix d'archi justifiés, "ce que je referais autrement".
- ✅ Fini quand : le repo est montrable à un recruteur tel quel.
- ➕ Si temps restant : GIF de démo dans le README.

### S8.5 — Rétrospective de phase 🏁
- 📖 (15 min) : relire tout le journal de la phase.
- 💻 (45 min) : écrire la rétro (vitesse réelle vs plan, confiance Python /10, ce qui mérite révision). Puis avec Claude : **générer le SESSIONS.md détaillé de la phase 2**, ajusté à la rétro.
- ✅ Fini quand : phase 1 cochée dans ROADMAP.md, SESSIONS.md phase 2 créé, milestone fermée.

---

## Lectures hors sessions (fil rouge, ~20 min/jour dans les transports)
- Semaines 1-4 : Chip Huyen ch. 1 — *Introduction to Building AI Applications with Foundation Models*.
- Semaines 5-8 : Chip Huyen ch. 2 — *Understanding Foundation Models*.
