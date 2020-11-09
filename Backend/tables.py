# tables.py
import flask_sqlalchemy
from server import db

class User(db.Model):
    email = db.Column(db.String(120), primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    organization = db.Column(db.String(120))
    descr = db.Column(db.String(250))
    user_type = db.Column(db.String(120))
    gen_link_1 = db.Column(db.String(250))
    gen_link_2 = db.Column(db.String(250))
    gen_link_3 = db.Column(db.String(250))
    image = db.Column(db.String(250))
    doc = db.Column(db.String(250))

    def __init__(self, e, fname, lname, org, des, u_type, gl1, gl2, gl3, img, d):
        self.email = e
        self.first_name = fname
        self.last_name = lname
        self.organization = org
        self.descr = des
        self.user_type = u_type
        self.gen_link_1 = gl1
        self.gen_link_2 = gl2
        self.gen_link_3 = gl3
        self.image = img
        self.doc = d

class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id1 = db.Column(db.String(128))
    user_id2 = db.Column(db.String(128))

    def __init__(self, user1, user2):
        self.user_id1 = user1
        self.user_id2 = user2

db.create_all()