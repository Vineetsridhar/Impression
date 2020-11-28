# server.py
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=no-member
# pylint: disable=wrong-import-position
# pylint: disable=broad-except

import os
from os.path import join, dirname
from dotenv import load_dotenv
import flask
import flask_sqlalchemy
import flask_socketio

################################

# Configuration and Variables

SERVER_PREFIX = "\033[96m" + "[SERVER]" + "\033[0m" + " "

dotenv_path = join(dirname(__file__), "secret.env")
load_dotenv(dotenv_path)

app = flask.Flask(__name__, template_folder="../LandingPage", static_folder="../LandingPage")

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

database_uri = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri


db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app

db.session.commit()

import imp_util
import tables
import users

clients = []

################################

#### Given info from a user login, creates new user

def create_new_user(data):
    try:
        fields = ["email", "given_name", "family_name", "picture"]
        for field in fields:
            if field not in data:
                data[field] = ""
        imp_util.users.new_user(
            data["email"], data["given_name"], data["family_name"], data["picture"]
        )
        imp_util.qr.create_new_qr_code(data["email"])
        return {"success": True, "email": data["email"]}
    except Exception as err:
        print(err)
        return {"success": False}

@app.route("/new_user", methods=["POST"])
def on_new_user():
    data = flask.request.json
    return create_new_user(data)


#### Given info from a user input, changes info of user on database
@app.route("/edit_user", methods=["POST"])
def on_edit():
    data = flask.request.json
    return imp_util.users.edit_user(data)


#### Given an email, returns a dictionary with the data of the user with such an email
@app.route("/get_user", methods=["POST"])
def get_user():
    query_user_email = flask.request.json
    return imp_util.users.get_user(query_user_email["email"])


@app.route("/upload_doc", methods=["POST"])
def on_upload_doc():
    form = flask.request.form
    data = flask.request.files["file"]
    data.save("temp/resume_%s.pdf" % form["email"])
    imp_util.s3.upload_pdf(form["email"])
    return {}

#### Given 2 user emails, adds them as a new connection
#### to the DB if such a connection does not already exist.
#### Returns -1 if such a connection already exists,
#### and 0 if the connection was added.
@app.route("/new_connection", methods=["POST"])
def on_new_connection():
    data = flask.request.json
    return imp_util.connections.on_new_connection(data)


#### Given 2 user emails,
#### remove the exisiting connection between them if it exists.
#### Returns -1 if such a connection does not exist,
#### and 0 if the connection existed and was deleted.
@app.route("/delete_connection", methods=["POST"])
def on_delete_connection():
    data = flask.request.json
    return imp_util.connections.on_delete_connection(data)


#### Given a user X's email, returns a list of users X has a connection with.
#### Specifically, it returns a list of dictionaries
#### where each dictionary is the data of a user X has a connection with.
#### Used to query for all connections involving a given user.
@app.route("/query_connections", methods=["POST"])
def on_query_connections():
    data = flask.request.json
    return {
        "success": True,
        "connections": imp_util.connections.on_query_connections(data),
    }


@app.route("/linkedin_login", methods=["POST"])
def on_linkedin_login():
    data = flask.request.json
    access_token = imp_util.linkedin.get_access_token(data["authorization_token"]["authentication_code"])
    #get user info 
    profile_info = imp_util.linkedin.get_profile(access_token)
    #get email
    email = imp_util.linkedin.get_user_email(access_token)
    #add to db
    profile_info["email"] = email
    return create_new_user(profile_info)

@app.route("/")
def index():
    return flask.render_template("index.html")


if __name__ == "__main__":
    socketio.run(
        app,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
