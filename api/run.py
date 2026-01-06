import os  # noqa: F401
import json  # noqa: F401
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
