# ✂️ split-long-text — Découper un long fichier texte en plusieurs parties

> **Un script Python simple, commenté et pédagogique** qui lit un fichier texte
> volumineux (`long_texte.txt`) et le découpe en plusieurs fichiers de
> **500 lignes maximum** (`partie_1.txt`, `partie_2.txt`, …), rangés dans un
> dossier `parties/`.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![PowerShell](https://img.shields.io/badge/PowerShell-7.6.9-blue.svg)
![OS](https://img.shields.io/badge/OS-Windows-lightgrey.svg)
![Licence](https://img.shields.io/badge/Licence-MIT-green.svg)

---

## 📖 Sommaire

- [🎯 Objectif du projet](#-objectif-du-projet)
- [🧠 Concepts pédagogiques abordés](#-concepts-pédagogiques-abordés)
- [📦 Prérequis](#-prérequis)
- [🚀 Démarrage rapide (PowerShell)](#-démarrage-rapide-powershell)
- [📁 Structure du dépôt](#-structure-du-dépôt)
- [⚙️ Configuration](#-configuration)
- [🔬 Explication du code, bloc par bloc](#-explication-du-code-bloc-par-bloc)
- [📤 Résultat attendu](#-résultat-attendu)
- [🛠️ Dépannage](#-dépannage)
- [🌱 Pistes d'amélioration](#-pistes-d-amélioration)
- [🤝 Contribuer](#-contribuer)
- [📄 Licence](#-licence)
- [👤 Auteur](#-auteur)

---

## 🎯 Objectif du projet

Il arrive souvent qu'un fichier texte soit **trop long** pour être manipulé
confortablement : envoi par e-mail limité en taille, outil qui n'accepte que
quelques milliers de lignes, impression papier, traitement séquentiel…

Ce projet répond à ce besoin très concret avec un script unique :

1. **Ouvre** le fichier source `long_texte.txt` en lecture seule ;
2. **Lit** son contenu paquet par paquet (500 lignes à la fois) ;
3. **Écrit** chaque paquet dans un fichier numéroté (`partie_1.txt`, …)
   dans le dossier `parties/` ;
4. **Affiche** un message de confirmation pour chaque partie créée.

### Ce que le script fait… et ne fait pas

| ✅ Fait | ❌ Ne fait pas (volontairement) |
|---|---|
| Découpe un fichier ligne par ligne | Ne modifie jamais le fichier d'origine |
| Crée le dossier de sortie automatiquement | Ne trie pas, ne dédoublonne pas les lignes |
| Tolère les caractères mal encodés | Ne découpe pas par taille en octets |
| Fonctionne sans dépendance externe | N'offre pas (encore) d'options en ligne de commande |

---

## 🧠 Concepts pédagogiques abordés

Ce dépôt est pensé comme un **support d'apprentissage**. En étudiant le code,
on rencontre notamment :

| Concept | Où le voir | Pourquoi c'est intéressant |
|---|---|---|
| `pathlib.Path` | Constantes `SOURCE`, `OUTPUT` | Alternative moderne et orientée objet à `os.path` |
| Gestionnaire de contexte `with` | Ouverture du fichier | Fermeture garantie du fichier, même en cas d'erreur |
| Encodage UTF-8 + `errors="replace"` | `SOURCE.open(...)` | Comprendre bytes vs texte, et éviter les crashs |
| Boucle sentinelle `while True` + `break` | Boucle principale | Pattern classique de lecture « jusqu'à épuisement » |
| `readline()` | Lecture ligne par ligne | Mémoire maîtrisée : jamais tout le fichier en RAM |
| Opérateur `/` de `Path` | `OUTPUT / f"partie_{part}.txt"` | Concaténation de chemins lisible et portable |
| f-strings | `print(f"Partie créée : {destination}")` | Interpolation de variables moderne et lisible |
| Garde `if __name__ == "__main__":` | Fin du script | Permet d'importer le module sans l'exécuter |

---

## 📦 Prérequis

- **Système** : Windows (le projet est développé et testé sous PowerShell 7.6.9) ;
- **Python** : version **3.10 ou supérieure** ;
- **Git** (optionnel) : uniquement pour cloner le dépôt ou publier vos modifications ;
- **Compte GitHub** : [@valorisa](https://github.com/valorisa) pour le dépôt distant.

Vérification rapide dans le terminal :

```powershell
python --version   # doit afficher Python 3.10 ou plus
```

> [!TIP]
> Si `python` n'est pas reconnu, essayez `py --version` (lanceur Windows),
> ou réinstallez Python en cochant bien la case **« Add python.exe to PATH »**.

---

## 🚀 Démarrage rapide (PowerShell)

Toute la session se déroule depuis le dossier de travail `C:\Users\bbrod\Projets`.

### Étape 0 — Se placer dans le dossier de travail

```powershell
PS C:\Users\bbrod> cd Projets
PS C:\Users\bbrod\Projets>
```

`cd` (*change directory*) déplace le terminal dans le dossier `Projets`.
Le prompt (`PS C:\Users\bbrod\Projets>`) confirme votre position actuelle.

### Étape 1 — Récupérer le code

**Option A — Cloner le dépôt GitHub :**

```powershell
git clone https://github.com/valorisa/split-long-text.git
cd split-long-text
```

**Option B — Créer le projet à la main :**

```powershell
mkdir split-long-text
cd split-long-text
notepad split_long_text.py    # ou: code split_long_text.py si vous avez VS Code
```

Collez le contenu du script (voir section suivante), enregistrez (`Ctrl+S`), fermez.

### Étape 2 — Créer un faux fichier source pour tester

Pas besoin d'un vrai gros fichier : PowerShell peut en générer un en une ligne.

```powershell
1..1200 | ForEach-Object { "Ligne $_ : ceci est un texte de démonstration." } |
    Set-Content -Path long_texte.txt -Encoding utf8
```

Décryptement de cette commande :

- `1..1200` : produit les entiers de 1 à 1200 ;
- `ForEach-Object { ... }` : transforme chaque entier en une ligne de texte (`$_` = entier courant) ;
- `Set-Content -Path ... -Encoding utf8` : écrit le tout dans `long_texte.txt` en UTF-8.

> [!NOTE]
> 1200 lignes ⇒ le script produira **3 parties** : 500 + 500 + 200 lignes.

### Étape 3 — Lancer le script

```powershell
python split_long_text.py
```

### Étape 4 — Constater le résultat

```powershell
Get-ChildItem parties          # alias possibles: ls parties  /  dir parties
```

---

## 📁 Structure du dépôt

```
split-long-text/
├── split_long_text.py    # ← le script principal (le cœur du projet)
├── README.md             # ← ce document
├── .gitignore            # ← fichiers à ne pas publier sur GitHub
├── long_texte.txt        # ← fichier source (créé par vous, non versionné)
└── parties/              # ← dossier généré par le script (non versionné)
    ├── partie_1.txt
    ├── partie_2.txt
    └── partie_3.txt
```

Contenu conseillé du `.gitignore` (les données générées restent locales) :

```gitignore
# Fichiers locaux / générés : on ne les publie pas
long_texte.txt
parties/
__pycache__/
```

---

## ⚙️ Configuration

Trois constantes en haut du script suffisent à tout régler :

| Variable | Valeur par défaut | Rôle |
|---|---|---|
| `SOURCE` | `Path("long_texte.txt")` | Chemin du fichier à découper |
| `OUTPUT` | `Path("parties")` | Dossier de destination des parties |
| `LINES_PER_FILE` | `500` | Nombre maximal de lignes par partie |

Exemple : pour des parties de 1 000 lignes dans un dossier `sortie/` :

```python
SOURCE = Path("mon_gros_fichier.txt")
OUTPUT = Path("sortie")
LINES_PER_FILE = 1000
```

> [!WARNING]
> Le dossier `OUTPUT` est créé automatiquement (`mkdir(exist_ok=True)`).
> S'il existe déjà, **son contenu n'est pas vidé** : les fichiers portant le
> même nom seront simplement écrasés.

---

## 🔬 Explication du code, bloc par bloc

Voici le script intégral, puis son analyse détaillée.

```python
from pathlib import Path

SOURCE = Path("long_texte.txt")
OUTPUT = Path("parties")
LINES_PER_FILE = 500


def split_file():
    OUTPUT.mkdir(exist_ok=True)

    with SOURCE.open(
        "r", encoding="utf-8", errors="replace"
    ) as file:
        part = 1
        while True:
            lines = []
            for _ in range(LINES_PER_FILE):
                line = file.readline()
                if not line:
                    break
                lines.append(line)

            if not lines:
                break
            destination = OUTPUT / f"partie_{part}.txt"
            destination.write_text(
                "".join(lines),
                encoding="utf-8"
            )
            print(f"Partie créée : {destination}")
            part += 1


if __name__ == "__main__":
    if SOURCE.is_file():
        split_file()
    else:
        print("Fichier introuvable.")
```

### Bloc 1 — Import et constantes

```python
from pathlib import Path

SOURCE = Path("long_texte.txt")
OUTPUT = Path("parties")
LINES_PER_FILE = 500
```

- `pathlib` est la boîte à outils **moderne** de manipulation de chemins de fichiers.
- Un objet `Path` représente un chemin, quel que soit l'OS (Windows, Linux, macOS).
- Les constantes en MAJUSCULES signalent des valeurs **destinées à être configurées**
  une seule fois, en haut du fichier.

### Bloc 2 — Préparer le dossier de sortie

```python
OUTPUT.mkdir(exist_ok=True)
```

- Crée le dossier `parties/` s'il n'existe pas.
- `exist_ok=True` : **ne pas lever d'erreur** si le dossier existe déjà.
  Sans cet argument, relancer le script provoquerait un crash `FileExistsError`.

### Bloc 3 — Ouvrir le fichier proprement

```python
with SOURCE.open(
    "r", encoding="utf-8", errors="replace"
) as file:
```

- `"r"` : mode **lecture seule** (*read*). Le fichier source ne peut pas être abîmé.
- `encoding="utf-8"` : interprète les octets comme du texte UTF-8 (le standard du web).
- `errors="replace"` : si un octet est invalide, il est remplacé par le caractère ``
  **au lieu de faire planter le script**. Choix assumé : privilégier la robustesse.
- `with ... as file` : à la sortie du bloc (même en cas d'exception), le fichier est
  **fermé automatiquement**. C'est la bonne pratique absolue en Python.

### Bloc 4 — La boucle de lecture « paquet par paquet »

```python
part = 1
while True:
    lines = []
    for _ in range(LINES_PER_FILE):
        line = file.readline()
        if not line:
            break
        lines.append(line)

    if not lines:
        break
```

- `part = 1` : numéro de la partie en cours de construction.
- `while True` : boucle infinie **sentinelle** ; on en sort uniquement via `break`.
- `lines = []` : tampon vidé à chaque tour : chaque partie repart de zéro.
- `for _ in range(LINES_PER_FILE)` : tente de lire 500 lignes. Le `_` est une
  convention : « cette variable de boucle ne nous intéresse pas ».
- `file.readline()` : lit **une** ligne, en gardant son `\n` final.
  À la fin du fichier, elle renvoie une chaîne vide `""`.
- `if not line: break` : fin du fichier détectée → on arrête de remplir le tampon.
- `if not lines: break` : si le tampon est vide (fichier fini, ou fichier vide
  dès le départ), on arrête totalement la boucle principale.

> [!NOTE]
> Pourquoi ne pas faire `file.readlines()` d'un coup ? Parce que sur un fichier de
> plusieurs millions de lignes, cela chargerait **tout** en mémoire vive.
> Ici, la mémoire utilisée reste proportionnelle à `LINES_PER_FILE` : c'est volontaire.

### Bloc 5 — Écrire la partie et passer à la suivante

```python
destination = OUTPUT / f"partie_{part}.txt"
destination.write_text(
    "".join(lines),
    encoding="utf-8"
)
print(f"Partie créée : {destination}")
part += 1
```

- `OUTPUT / f"partie_{part}.txt"` : l'opérateur `/** construit un chemin
  (`parties\partie_1.txt` sous Windows) de façon lisible et portable.
- `"".join(lines)` : recolle les lignes (qui contiennent déjà leur `\n`)
  en un seul texte. Aucun séparateur ajouté : le contenu est **identique** à l'original.
- `write_text(..., encoding="utf-8")` : écrit le fichier en une seule opération.
- `print(f"...")` : feedback immédiat à l'utilisateur — un script silencieux est
  un script anxiogène.
- `part += 1` : on passe au numéro suivant, puis la boucle `while True` repart.

### Bloc 6 — La garde d'exécution

```python
if __name__ == "__main__":
    if SOURCE.is_file():
        split_file()
    else:
        print("Fichier introuvable.")
```

- `__name__` vaut `"__main__"` **seulement** quand le script est lancé directement
  (`python split_long_text.py`). Si quelqu'un fait `import split_long_text`,
  rien ne s'exécute : le module reste utilisable (tests, réutilisation…).
- `SOURCE.is_file()` : vérification conviviale avant de travailler. Si le fichier
  manque, un message clair (« Fichier introuvable. ») remplace une stacktrace effrayante.

---

## 📤 Résultat attendu

Session complète et réaliste sous PowerShell 7.6.9 :

```powershell
PS C:\Users\bbrod> cd Projets
PS C:\Users\bbrod\Projets> cd split-long-text
PS C:\Users\bbrod\Projets\split-long-text> python split_long_text.py
Partie créée : parties\partie_1.txt
Partie créée : parties\partie_2.txt
Partie créée : parties\partie_3.txt
PS C:\Users\bbrod\Projets\split-long-text> Get-ChildItem parties

    Directory: C:\Users\bbrod\Projets\split-long-text\parties

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          06/11/2026    10:15          24890 partie_1.txt
-a---          06/11/2026    10:15          24890 partie_2.txt
-a---          06/11/2026    10:15           9956 partie_3.txt
```

> [!NOTE]
> Sous Windows, les chemins affichés utilisent des antislashes (`parties\partie_1.txt`) :
> c'est le comportement normal de `pathlib`, qui adapte le séparateur à l'OS.

---

## 🛠️ Dépannage

| Symptôme | Cause probable | Solution |
|---|---|---|
| `Fichier introuvable.` | `long_texte.txt` absent du dossier courant | Créez-le (étape 2) ou ajustez `SOURCE` |
| `python : The term 'python' is not recognized` | Python absent du `PATH` | Utilisez `py split_long_text.py`, ou réinstallez Python avec l'option PATH |
| Caractères `` dans les parties | Octets invalides dans le source | Comportement **voulu** (`errors="replace"`) : le script privilégie la continuité |
| `PermissionError` | Fichier ouvert dans un autre programme | Fermez l'éditeur ou le lecteur qui verrouille le fichier |
| Aucune partie créée, aucun message | Fichier source vide | Normal : rien à découper. Ajoutez du contenu ou vérifiez le chemin |
| Le script découpe le mauvais fichier | Mauvais dossier courant | Vérifiez le prompt PowerShell : `split_long_text.py` doit être dans le dossier actuel (`Get-ChildItem` pour contrôler) |

---

## 🌱 Pistes d'amélioration

Quelques idées pour aller plus loin (contributions bienvenues !) :

- [ ] Arguments en ligne de commande avec `argparse`
      (`python split_long_text.py --lignes 1000 --source mon_fichier.txt`) ;
- [ ] Numérotation avec zéros de remplissage : `partie_001.txt` (tri alphabétique correct) ;
- [ ] Journalisation avec le module `logging` plutôt que `print` ;
- [ ] Tests automatisés avec `pytest` (fichier vide, fichier de 499 lignes, encodage cassé…) ;
- [ ] Barre de progression avec `tqdm` pour les fichiers énormes ;
- [ ] Découpage par taille (en Mo) plutôt qu'en nombre de lignes.

---

## 🤝 Contribuer

1. **Fork** le dépôt ;
2. Créez une branche : `git switch -c ma-fonctionnalite` ;
3. Commitez vos changements : `git commit -m "Description claire"` ;
4. Poussez : `git push origin ma-fonctionnalite` ;
5. Ouvrez une **Pull Request** sur le dépôt de `valorisa`.

Merci de garder un code simple, commenté et lisible : c'est l'esprit du projet. 🙏

---

## 📄 Licence

Projet distribué sous licence **MIT** : utilisation, modification et redistribution
libres, y compris à des fins commerciales, à condition de conserver la mention d'origine.

Copyright (c) 2026 valorisa

---

## 👤 Auteur

**valorisa** — [github.com/valorisa](https://github.com/valorisa)

Développé et testé sous **PowerShell 7.6.9**, depuis le poste de travail
`C:\Users\bbrod\Projets` (Windows).

---

<p align="center">
  <a href="#-split-long-text--découper-un-long-fichier-texte-en-plusieurs-parties">⬆️ Retour en haut</a>
</p>
