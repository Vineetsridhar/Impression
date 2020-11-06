# app.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import datetime
import flask
import flask_sqlalchemy
import flask_socketio

import tables

################################

# Configuration and Variables

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

app.config["SQLALCHEMY_DATABASE_URI"] = TODO
db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app
db.create_all()
db.session.commit()

################################

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
    for connection in db.session.query(tables.Connection).all():
        if connection.userID1 == data["queryUser"] or connection.userID2 == data["queryUser"]:
            result.append(connection)
    
    for connection in result:
        TODO
    