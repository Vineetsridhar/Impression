# tables.py
# pylint: disable=too-many-instance-attributes
# pylint: disable=missing-function-docstring
# pylint: disable=no-member
# pylint: disable=too-many-arguments
# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=missing-module-docstring
# pylint: disable=unused-import

import flask_sqlalchemy
from server import db


class Users(db.Model):
    email = db.Column(db.String(120), primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    organization = db.Column(db.String(120), nullable=True)
    descr = db.Column(db.String(250), nullable=True)
    user_type = db.Column(db.String(120), nullable=True)
    gen_link_1 = db.Column(db.String(250), nullable=True)
    gen_link_2 = db.Column(db.String(250), nullable=True)
    gen_link_3 = db.Column(db.String(250), nullable=True)
    image = db.Column(db.String(250))
    doc = db.Column(db.String(250), nullable=True)

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


class Connections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1_email = db.Column(db.String(128))
    user2_email = db.Column(db.String(128))

    def __init__(self, user1, user2):
        self.user1_email = user1
        self.user2_email = user2

class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(120))
    user1_email = db.Column(db.String(120))
    user2_email = db.Column(db.String(120))
    user3_email = db.Column(db.String(120))
    user4_email = db.Column(db.String(120))
    user5_email = db.Column(db.String(120))

    def __init__(self, gn, us1em, us2em, us3em, us4em, us5em):
        self.group_name = gn
        self.user1_email = us1em
        self.user2_email = us2em
        self.user3_email = us3em
        self.user4_email = us4em
        self.user5_email = us5em

db.create_all()
