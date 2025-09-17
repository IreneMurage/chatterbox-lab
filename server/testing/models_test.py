from datetime import datetime
import pytest

from app import app
from models import db, Message

@pytest.fixture(autouse=True)
def clean_db():
    """Clean DB before each test."""
    with app.app_context():
        db.session.query(Message).delete()
        db.session.commit()
    yield
    with app.app_context():
        db.session.query(Message).delete()
        db.session.commit()


class TestMessage:
    '''Message model in models.py'''

    def test_has_correct_columns(self):
        with app.app_context():
            hello_from_liza = Message(body="Hello 👋", username="Liza")
            db.session.add(hello_from_liza)
            db.session.commit()

            assert hello_from_liza.body == "Hello 👋"
            assert hello_from_liza.username == "Liza"
            assert isinstance(hello_from_liza.created_at, datetime)
