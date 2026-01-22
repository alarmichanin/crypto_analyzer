from flask import Blueprint

health_check_bp = Blueprint("health_check", __name__)


@health_check_bp.route("/health", methods=["GET"])
def health_check():
    return "ok", 200
