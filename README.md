# parc-informatique
projet de gestion des équipements informatiques
# 🖥️ Gestion du Parc Informatique

Application de bureau développée en **Python / Tkinter** dans le cadre d'un TP de programmation IHM.  
Elle permet de gérer l'ensemble des équipements informatiques d'un établissement (ajout, recherche, modification, suppression, affichage).


<img width="500" height="250" alt="TOUT" src="https://github.com/user-attachments/assets/245c32f0-a59f-40e2-b5ba-2d32e2727dbd" />


---

##  Fonctionnalités

-  **Ajouter** un équipement avec contrôle du numéro de série unique
  <img width="338" height="344" alt="AJOUT" src="https://github.com/user-attachments/assets/d0332e8f-5b29-442b-8641-387a33279b7a" />            <img width="283" height="159" alt="SUCCES D&#39;AJOUT" src="https://github.com/user-attachments/assets/8e3d0a7b-c9df-4c87-8e58-5a8ad78aefec" />
   

-  **Rechercher** par type, localisation, état ou numéro de série

  <img width="454" height="245" alt="RECHERCHE" src="https://github.com/user-attachments/assets/dc417ccc-050f-4544-95c2-0c9e6c161c4f" />

-  **Modifier** les informations d'un équipement existant

  <img width="626" height="396" alt="MODIFIER" src="https://github.com/user-attachments/assets/f2274472-0f2d-4cc0-aa94-29c3a24076f1" />            <img width="430" height="249" alt="SUCCES DE MODIFICATION" src="https://github.com/user-attachments/assets/53c78fa8-573f-4582-9713-44377e17089f" />


-  **Supprimer** un équipement avec confirmation

  <img width="413" height="249" alt="SUPP" src="https://github.com/user-attachments/assets/396f7e3e-88f5-44a9-8d97-d31d3c110587" />         <img width="217" height="122" alt="SUCCES DE SUPPRESSION" src="https://github.com/user-attachments/assets/d589282f-423a-42e1-a49e-ab86c5b2c2c1" />


-  **Afficher** tout le parc, triable par type ou localisation
-  **Coloration** des lignes selon l'état de l'équipement
-  **Statistiques** en temps réel dans le panneau latéral


<img width="326" height="491" alt="STAT" src="https://github.com/user-attachments/assets/120efe0e-6135-4355-af74-90de25854b22" />

---

##  Structure du projet
```
📁 projet/
├── main.py          # Point d'entrée de l'application
├── vue.py           # Interface graphique (Tkinter)
├── controlleur.py   # Logique de l'interface et actions
├── model.py         # Accès à la base de données SQLite
└── projetihm.db     # Base de données (créée automatiquement)
```

---

##  Prérequis

- Python **3.8** 
- Tkinter (inclus par défaut avec Python)
- Aucune bibliothèque externe à installer

---

##  Lancement
```bash
# Cloner le dépôt
git clone https://github.com/Imene06-hub/parc-informatique.git
cd parc-informatique

# Lancer l'application
python main.py
```

---

##  Base de données

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

##  Code couleur des états

| Couleur | État |
|---------|------|
| 🟢 Vert pâle | Opérationnel |
| 🟡 Jaune pâle | En panne |
| 🔴 Rouge pâle | Hors service |
| 🔵 Bleu pâle | Prêté |

---

##  Architecture MVC

Le projet suit le patron **Modèle - Vue - Contrôleur** :

- **`model.py`** — Toutes les opérations sur la base de données (SQLite)
- **`vue.py`** — Construction de l'interface graphique, aucune logique métier
- **`controlleur.py`** — Fait le lien entre la vue et le modèle, gère les actions utilisateur

---

##  Auteur

Projet réalisé dans le cadre d'un TP — Module IHM  
**MEDANI Imene** — UMMTO
