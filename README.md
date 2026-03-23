

# Blog API - Gestion d'articles

Une API REST simple pour gérer des articles de blog, développée avec Flask.

## Installation

1. **Cloner le projet**
```bash
git clone <votre-repo>
cd <nom-du-dossier>

    Installer les dépendances

bash

pip install flask flask-sqlalchemy

    Lancer l'application

bash

python app.py

L'API sera accessible à : http://localhost:5000
Endpoints API
Méthode	URL	Description
POST	/api/articles	Créer un article
GET	/api/articles	Lister tous les articles
GET	/api/articles/<id>	Afficher un article
PUT	/api/articles/<id>	Modifier un article
DELETE	/api/articles/<id>	Supprimer un article
GET	/api/articles/search?q=mot-cle	Rechercher des articles
Exemples d'utilisation
Créer un article
bash

curl -X POST http://localhost:5000/api/articles \
  -H "Content-Type: application/json" \
  -d '{"title":"Mon article","content":"Contenu de l'article"}'

Lister tous les articles
bash

curl http://localhost:5000/api/articles

Structure du projet
text

├── app.py           # Point d'entrée principal
├── model.py         # Modèle Article
├── routes.py        # Routes de l'API
├── extensions.py    # Extension SQLAlchemy
└── blog.db          # Base de données SQLite (créée automatiquement)

Technologies

    Flask

    Flask-SQLAlchemy

    SQLite
