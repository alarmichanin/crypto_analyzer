import os
from dotenv import load_dotenv
from flask import Flask
from app.routes.health import health_check_bp
from app.db import db, migrate
from redis import Redis

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["REDIS_HOST"] = os.getenv("REDIS_HOST", "localhost")
app.config["REDIS_PORT"] = os.getenv("REDIS_PORT", "6379")
app.config["REDIS_DB"] = 0

redis = Redis(app)

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(health_check_bp)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    debug_value = os.getenv("FLASK_DEBUG", "0").strip().lower()
    debug = debug_value in ("1", "true", "yes", "y", "on")

    app.run(host="0.0.0.0", port=port, debug=debug)
