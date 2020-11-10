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

import users
import tables

################################

# got rid of user ID for users
# TODO: change filter_by
def get_user(query_user_id):
    user = tables.User.query.filter_by(user_id=query_user_id).first()
    response = {
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "organization": user.organization,
        "descr": user.descr,
        "user_type": user.user_type,
        "gen_link_1": user.gen_link_1,
        "gen_link_2": user.gen_link_2,
        "gen_link_3": user.gen_link_3,
        "image": user.image,
        "doc": user.doc,
    }
    return response

# TODO: change filter_by
@socketio.on("new connection")
def on_new_connection(data):
    for connection in db.session.query(tables.Connection) .all():
        if (
            connection.user_id1 == data["user_id1"]
            and connection.user_id2 == data["user_id2"]
        ):
            return
        elif (
            connection.user_id1 == data["user_id2"]
            or connection.user_id2 == data["user_id1"]
        ):
            return

    db.session.add(tables.Connection(data["user_id1"], data["user_id2"]))
    db.session.commit()

# TODO: change filter_by
@socketio.on("query connections")
def on_query_connections(data):
    result = []
    response = []
    for connection in db.session.query(tables.Connection).all():
        if (
            connection.user_id1 == data["queryUser"]
            or connection.user_id2 == data["queryUser"]
        ):
            result.append(connection)

    for connection in result:
        if data["queryUser"] == connection.user_id1:
            pass
        else:
            pass
    response.append({})  # UserID, Name, Description, Email, User Typ

@app.route("/")
def index():
    return tables.Connection.query.filter_by(user1_email="test1").first().user2_email

if __name__ == "__main__":
    socketio.run(
        app,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )