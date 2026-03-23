from flask import Flask, jsonify
import os

from extensions import db
from routes import article_bp


def create_app():
    app = Flask(__name__)

    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, "blog.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_AS_ASCII"] = False

    db.init_app(app)

    with app.app_context():
        from model import Article
        db.create_all()

    app.register_blueprint(article_bp, url_prefix="/api")

    @app.get("/")
    def home():
        return jsonify({
            "message": "API REST Flask pour la gestion des articles de blog",
            "version": "1.0.0",
            "endpoints": {
                "creer_article": "POST /api/articles",
                "afficher_article": "GET /api/articles/<id>",
                "lister_articles": "GET /api/articles",
                "modifier_article": "PUT /api/articles/<id>",
                "supprimer_article": "DELETE /api/articles/<id>",
                "rechercher_article": "GET /api/articles/search?q=mot-cle"
            }
        })

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
