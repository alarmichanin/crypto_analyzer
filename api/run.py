import os
import json
from dotenv import load_dotenv
from flask import Flask
from app.routes.health import health_check_bp

load_dotenv()

app = Flask(__name__)

app.register_blueprint(health_check_bp)

if __name__ == "__main__":
    app.run(debug=True)