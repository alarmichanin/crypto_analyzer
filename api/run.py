import os
import json
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)