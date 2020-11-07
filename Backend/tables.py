# models.py
import flask_sqlalchemy
from server import db

class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID1 = db.Column(db.String(128))
    userID2 = db.Column(db.String(128))

    def __init__(self, user1, user2):
        self.userID1 = user1
        self.userID2 = user2

db.create_all()
