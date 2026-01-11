from flask import Blueprint

<<<<<<< HEAD
health_check_bp = Blueprint("health_check", __name__)


@health_check_bp.route("/health", methods=["GET"])
=======
health_check_bp = Blueprint(
    "health_check",
    __name__,
)


@health_check_bp.route("/health")
>>>>>>> bc20053a1818a08eee58cf27da113277832af0c0
def health_check():
    return "ok", 200
