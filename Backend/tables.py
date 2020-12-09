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
from sqlalchemy.orm import relationship
from server import DB

class Users(DB.Model):
    email = DB.Column(DB.String(120), primary_key=True)
    first_name = DB.Column(DB.String(120))
    last_name = DB.Column(DB.String(120))
    organization = DB.Column(DB.String(120), nullable=True)
    descr = DB.Column(DB.String(250), nullable=True)
    user_type = DB.Column(DB.String(120), nullable=True)
    gen_link_1 = DB.Column(DB.String(250), nullable=True)
    gen_link_2 = DB.Column(DB.String(250), nullable=True)
    gen_link_3 = DB.Column(DB.String(250), nullable=True)
    image = DB.Column(DB.String(250))
    doc = DB.Column(DB.String(250), nullable=True)

    def __init__(self, email, fname, lname, org, des, u_type, gl1, gl2, gl3, img, doc):
        self.email = email
        self.first_name = fname
        self.last_name = lname
        self.organization = org
        self.descr = des
        self.user_type = u_type
        self.gen_link_1 = gl1
        self.gen_link_2 = gl2
        self.gen_link_3 = gl3
        self.image = img
        self.doc = doc


class Connections(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    user1_email = DB.Column(DB.String(128))
    user2_email = DB.Column(DB.String(128))

    def __init__(self, user1, user2):
        self.user1_email = user1
        self.user2_email = user2


class Groups(DB.Model):
    group_id = DB.Column(DB.Integer, primary_key=True)
    user_email = DB.Column(
        DB.String(120), DB.ForeignKey("users.email"), primary_key=True
    )
    group_name = DB.Column(DB.String(128))

    def __init__(self, g_id, g_name, u_em):
        self.group_id = g_id
        self.group_name = g_name
        self.user_email = u_em
        

class geo_loc(DB.Model):
    email = DB.Column(DB.String(128), primary_key=True)
    latitude = DB.Column(DB.Float(16))
    longitude = DB.Column(DB.Float(16))
    
    def __init__(self, ema, lat, lon):
        self.email = ema
        self.latitude = lat
        self.longitude = lon

DB.create_all()
