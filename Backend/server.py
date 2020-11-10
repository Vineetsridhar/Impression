# server.py
import os
import datetime
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import flask
import flask_sqlalchemy
import flask_socketio

################################

# Configuration and Variables

SERVER_PREFIX = '\033[96m' + "[SERVER]" + '\033[0m' + " "

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

clients = []

################################

#### Given info from a user login, creates new user
@app.route("/new_user", methods=["POST"])
def on_new_user():
    data = flask.request.json
    try:
        fields = ["email", "given_name", "family_name", "picture"]
        for field in fields:
            if field not in data:
                data[field] = ""
        ImpUtil.Users.new_user(data["email"], data["given_name"], data["family_name"], data["picture"])
        return {"success":True, "email":data["email"]}
    except:
        return {"success": False}

#### Given info from a user input, changes info of user on database
@socketio.on("edit user")
def on_edit(data):
    ImpUtil.Users.edit_user(data)

@socketio.on("login")
def on_login(data):
    clients.append({"email": data["user_email"], "room": flask.session.get('room'), "sid": flask.request.sid}) 
    print(SERVER_PREFIX + str(clients[0]))

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
@app.route("/query_connections")
def on_query_connections():
    data = flask.request.json
    return {
        "success":True,
        "status": 0,
        "response": ImpUtil.Connections.on_query_connections(data), #Make sure you add error checking to this
    },
    
@app.route("/")
def index():
    db.session.add(tables.Connections("test1", "test2"))
    db.session.add(tables.Connections("test3", "test4"))
    db.session.commit()
    return tables.Connections.query.filter_by(user2_email="test4").first().user1_email

if __name__ == "__main__":
    socketio.run(
        app,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )