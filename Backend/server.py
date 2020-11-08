# app.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import datetime
import flask
import flask_sqlalchemy
import flask_socketio
from flask_restful import Resource, Api

################################

# Configuration and Variables
dotenv_path = join(dirname(__file__), "secret.env")
load_dotenv(dotenv_path)

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

database_uri = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app
db.session.commit()

import tables

################################

def get_user(userID):
    user = tables.User.query.filter_by(user_id=userID).first()
    response =  {"email": user.email, "user_id": user.user_id, "first_name": user.first_name, "last_name": user.last_name, "descr": user.descr, "user_type": user.user_type, "gen_link_1": user.gen_link_1, "gen_link_2": user.gen_link_2, "gen_link_3": user.gen_link_3, "image": user.image, "doc": user.doc}
    return response

def change_fname(userID, fname):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.first_name = fname
    db.session.commit()
    
def change_lname(userID, lname):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.last_name = lname
    db.session.commit()
    
def change_email(userID, em):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.email = em
    db.session.commit()
    
def change_descr(userID, des):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.descr = des
    db.session.commit()

def change_genlink1(userID, genlink1):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.gen_link_1 = genlink1
    db.session.commit()

def change_genlink2(userID, genlink2):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.gen_link_2 = genlink2
    db.session.commit()

def change_genlink3(userID, genlink3):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.gen_link_3 = genlink3
    db.session.commit()

def change_img(userID, im):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.image = im
    db.session.commit()

def change_doc(userID, document):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.doc = document
    db.session.commit()

def change_type(userID, usertype):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.user_type = usertype
    db.session.commit()
    
@socketio.on("new connection")
def on_new_connection(data):
    for connection in db.session.query(tables.Connection).all():
        if connection.userID1 == data["userID1"] and connection.userID2 == data["userID2"]:
            return
        elif connection.userID1 == data["userID2"] or connection.userID2 == data["userID1"]:
            return
    
    db.session.add(tables.Connection(data["userID1"], data["userID2"]))
    db.session.commit()
    
@socketio.on("query connections")
def on_query_connections(data):
    result = []
    response = []
    for connection in db.session.query(tables.Connection).all():
        if connection.userID1 == data["queryUser"] or connection.userID2 == data["queryUser"]:
            result.append(connection)
    
    for connection in result:
        if data["queryUser"] == connection.userID1:
            pass
        else:
            pass
        response.append({}) #UserID, Name, Description, Email, User Typ

@app.route("/")
def index():
    # emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)
    return "Hello World"

if __name__ == '__main__':
    app.run(port=8080)