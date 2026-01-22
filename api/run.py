import os

from app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    debug_value = os.getenv("FLASK_DEBUG", "0").strip().lower()
    debug = debug_value in ("1", "true", "yes", "y", "on")
    app.run(host="0.0.0.0", port=port, debug=debug)
