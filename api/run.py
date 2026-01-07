import os
# import json
from dotenv import load_dotenv
from flask import Flask
from app.routes.health import health_check_bp
from app.db import db, migrate

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(health_check_bp)

if __name__ == "__main__":
    app.run(debug=True)
