import os
from dotenv import load_dotenv
from flask import Flask
from app.routes.health import health_check_bp
from app.db import db, migrate
from app.models import User, Analysis, Probability  # noqa: F401

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(health_check_bp)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    debug_value = os.getenv("FLASK_DEBUG", "0").strip().lower()
    debug = debug_value in ("1", "true", "yes", "y", "on")
    db.create_all()
    app.run(host="0.0.0.0", port=port, debug=debug)
