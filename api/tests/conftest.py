import os

import pytest
from app import create_app, db


@pytest.fixture
def app():
    database_url = os.getenv("DATABASE_URL")

    if not database_url or "@db" in database_url or "localhost" in database_url:
        database_url = "sqlite:///:memory:"

    test_config = {"TESTING": True, "SQLALCHEMY_DATABASE_URI": database_url}

    app = create_app(test_config)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
