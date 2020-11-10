# server.py
import os
import datetime
from os.path import join, dirname
from dotenv import load_dotenv
import requests
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

database_uri = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app

db.session.commit()

import ImpUtil
import tables

################################

#### Given an email, returns a dictionary with the data of the user with such an email
def get_user(query_user_email):
    ImpUtil.Connections.get_user(query_user_email)
    
#### Given 2 user emails, adds them as a new connection to the DB if such a connection does not already exist.
#### Returns -1 if such a connection already exists, and 0 if the connection was added.
@socketio.on("new connection")
def on_new_connection(data):
    ImpUtil.Connections.on_new_connection(data)

#### Given 2 user emails, remove the exisiting connection between them if it exists.
#### Returns -1 if such a connection does not exist, and 0 if the connection existed and was deleted.
@socketio.on("delete connection")
def on_delete_connection(data):
    ImpUtil.Connections.on_delete_connection(data)

#### Given a user X's email, returns a list of users X has a connection with. Specifically, it returns a list of dictionaries where each dictionary is the data of a user X has a connection with.
#### Used to query for all connections involving a given user.
@socketio.on("query connections")
def on_query_connections(data):
    ImpUtil.Connections.on_query_connections(data)

@app.route("/")
def index():
    db.session.add(tables.Connection("test1", "test2"))
    db.session.add(tables.Connection("test3", "test4"))
    db.session.commit()
    return tables.Connection.query.filter_by(user2_email="test4").first().user1_email

if __name__ == "__main__":
    socketio.run(
        app,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )