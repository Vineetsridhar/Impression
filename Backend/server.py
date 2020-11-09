# app.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import datetime
import flask
import flask_sqlalchemy
import flask_socketio
from flask_restful import Resource, Api
import requests

################################

# Configuration and Variables
dotenv_path = join(dirname(__file__), "secret.env")
load_dotenv(dotenv_path)

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

database_uri = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app

db.session.commit()

import loader
import tables

################################

def get_user(userID):
    user = tables.User.query.filter_by(user_id=userID).first()
    response =  {"email": user.email, "user_id": user.user_id, "first_name": user.first_name, "last_name": user.last_name, "descr": user.descr, "user_type": user.user_type, "gen_link_1": user.gen_link_1, "gen_link_2": user.gen_link_2, "gen_link_3": user.gen_link_3, "image": user.image, "doc": user.doc}
    return response
    
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
    return tables.Connection.query.filter_by(userID1="test1").first().userID2

if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )