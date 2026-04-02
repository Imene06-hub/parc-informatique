# parc-informatique
projet de gestion des équipements informatiques
# 🖥️ Gestion du Parc Informatique

Application de bureau développée en **Python / Tkinter** dans le cadre d'un TP de programmation IHM.  
Elle permet de gérer l'ensemble des équipements informatiques d'un établissement (ajout, recherche, modification, suppression, affichage).

---

## 📋 Fonctionnalités

- ➕ **Ajouter** un équipement avec contrôle du numéro de série unique
- 🔍 **Rechercher** par type, localisation, état ou numéro de série
- ✏️ **Modifier** les informations d'un équipement existant
- 🗑️ **Supprimer** un équipement avec confirmation
- 📋 **Afficher** tout le parc, triable par type ou localisation
- 🎨 **Coloration** des lignes selon l'état de l'équipement
- 📊 **Statistiques** en temps réel dans le panneau latéral

---

## 🗂️ Structure du projet
```
📁 projet/
├── main.py          # Point d'entrée de l'application
├── vue.py           # Interface graphique (Tkinter)
├── controlleur.py   # Logique de l'interface et actions
├── model.py         # Accès à la base de données SQLite
└── projetihm.db     # Base de données (créée automatiquement)
```

---

## ⚙️ Prérequis

- Python **3.8** ou supérieur
- Tkinter (inclus par défaut avec Python)
- Aucune bibliothèque externe à installer

---

## 🚀 Lancement
```bash
# Cloner le dépôt
git clone https://github.com/TON_USERNAME/TON_REPO.git
cd TON_REPO

# Lancer l'application
python main.py
```

---

## 🗄️ Base de données

La base SQLite `projetihm.db` est créée automatiquement au premier lancement.  
Elle contient une seule table `equipements` avec les colonnes suivantes :

| Colonne | Type | Description |
|---------|------|-------------|
| id | INTEGER | Identifiant auto-incrémenté |
| type | TEXT | Type d'équipement (PC, Portable…) |
| marque | TEXT | Marque |
| modele | TEXT | Modèle |
| num_serie | TEXT | Numéro de série *(unique)* |
| localisation | TEXT | Bureau, Salle, Bâtiment |
| etat | TEXT | Opérationnel, En panne, Hors Service, Prêté |

---

## 🎨 Code couleur des états

| Couleur | État |
|---------|------|
| 🟢 Vert pâle | Opérationnel |
| 🟡 Jaune pâle | En panne |
| 🔴 Rouge pâle | Hors service |
| 🔵 Bleu pâle | Prêté |

---

## 🏗️ Architecture MVC

Le projet suit le patron **Modèle - Vue - Contrôleur** :

- **`model.py`** — Toutes les opérations sur la base de données (SQLite)
- **`vue.py`** — Construction de l'interface graphique, aucune logique métier
- **`controlleur.py`** — Fait le lien entre la vue et le modèle, gère les actions utilisateur

---

## 👨‍💻 Auteur

Projet réalisé dans le cadre d'un TP — Module IHM  
**MEDANI Imene** — [UMMTO]
