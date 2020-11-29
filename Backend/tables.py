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
from sqlalchemy.orm import relationship

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
    group_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), db.ForeignKey("users.email"), primary_key=True)
    group_name = db.Column(db.String(128))
    
    def __init__(self, g_id, g_name, u_em):
        self.group_id = g_id
        self.group_name = g_name
        self.user_email = u_em


class Notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120))
    title = db.Column(db.String(128))
    description = db.Column(db.String(128))
    type = db.Column(db.String(128))
    data1 = db.Column(db.String(256))
    data2 = db.Column(db.String(256))
    data3 = db.Column(db.String(256))
    data4 = db.Column(db.String(256))
    
    def __init__(self, email, titl, desc, type, data1, data2, data3, data4):
        self.user_email = email
        self.title = titl
        self.description = desc
        self.type = type
        self.data1 = data1
        self.data1 = data2
        self.data1 = data3
        self.data1 = data4

db.create_all()
