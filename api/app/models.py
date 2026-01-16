from datetime import datetime
from sqlalchemy.sql import expression
from app.db import db
import uuid


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(
        db.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(120), unique=True)
    tg_id = db.Column(db.String(9), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(
        db.Boolean,
        server_default=expression.false(),
        nullable=False,
    )

    def __init__(
        self,
        username=None,
        email=None,
        password_hash=None,
        tg_id=None,
    ):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.tg_id = tg_id

    def __repr__(self):
        return f"<User {self.username!r}>"


class Analysis(db.Model):
    __tablename__ = "analysis"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
    )
    coin = db.Column(db.String(120))
    percent = db.Column(db.Float, nullable=False)
    start_at = db.Column(db.DateTime, default=datetime.utcnow)
    end_at = db.Column(db.DateTime, default=datetime.utcnow)
    best_probability = db.Column(
        db.Integer, db.ForeignKey("probability.id"), nullable=False
    )

    def __init__(
        self,
        user_id=None,
        coin=None,
        percent=None,
    ):
        self.user_id = user_id
        self.coin = coin
        self.percent = percent

    def __repr__(self):
        return f"<Analysis {self.id!r}>"


class Probability(db.Model):
    __tablename__ = "probability"
    id = db.Column(db.Integer, primary_key=True)
    analysis_id = db.Column(
        db.Integer,
        db.ForeignKey("analysis.id"),
        nullable=False,
    )
    date = db.Column(db.DateTime, default=datetime.utcnow)
    probability = db.Column(db.Float, nullable=False)

    def __init__(
        self,
        analysis_id=None,
        date=None,
        probability=None,
    ):
        self.analysis_id = analysis_id
        self.date = date
        self.probability = probability

    def __repr__(self):
        return f"<Probability {self.id!r}>"
