import os

from app.db import db, migrate
from app.routes.health import health_check_bp
from dotenv import load_dotenv
from flask import Flask


def create_app(test_config=None):
    load_dotenv()

    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config:
        app.config.update(test_config)
    else:
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise RuntimeError(
                "DATABASE_URL is not set. "
                "Set it in .env (locally) or GitHub Secrets (CI)."
            )
        app.config["SQLALCHEMY_DATABASE_URI"] = database_url

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(health_check_bp)

    return app
