import os
<<<<<<< HEAD

from app.db import db, migrate
from app.routes.health import health_check_bp
=======
>>>>>>> bc20053a1818a08eee58cf27da113277832af0c0
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

<<<<<<< HEAD
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

=======
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "postgresql+psycopg2://postgres:postgres@db:5432/myappdb"
)
>>>>>>> bc20053a1818a08eee58cf27da113277832af0c0
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(health_check_bp)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    debug_value = os.getenv("FLASK_DEBUG", "0").strip().lower()
    debug = debug_value in ("1", "true", "yes", "y", "on")

    app.run(host="0.0.0.0", port=port, debug=debug)
