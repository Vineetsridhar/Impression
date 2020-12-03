# server.py
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=no-member
# pylint: disable=wrong-import-position
# pylint: disable=broad-except

import os
from os.path import join, dirname
import flask
import flask_sqlalchemy
import flask_socketio
from dotenv import load_dotenv

################################

# Values for index.html

PAGE_TITLE = "Grow your network with Impression"

PAGE_HEADER = "Easily connect with classmates and recruiters at your schools Career Fair"

DEVELOPER_NAMES = {
    "Chris": "Chris Mazzei",
    "Vineet": "Vineet Sridhar",
    "Rami": "Rami Bazoqa",
    "Stephanie": "Stephanie Nieve-Silva",
}

ABOUT_ME = {
    "Chris": "About Me.",
    "Vineet": "About Me.",
    "Rami": "About Me.",
    "Stephanie": "About Me.",
}

LINKS = {"Chris": "Links.", "Vineet": "Links.", "Rami": "Links.", "Stephanie": "Links."}

CONTACT_INFO = {
    "Chris": "Contact Info.",
    "Vineet": "Contact Info.",
    "Rami": "Contact Info.",
    "Stephanie": "Contact Info.",
}
################################

# Configuration and Variables

SERVER_PREFIX = "\033[96m" + "[SERVER]" + "\033[0m" + " "

DOTENV_PATH = join(dirname(__file__), "secret.env")
load_dotenv(DOTENV_PATH)

APP = flask.Flask(
    __name__, template_folder="../LandingPage", static_folder="../LandingPage"
)

SOCKETIO = flask_socketio.SocketIO(APP)
SOCKETIO.init_app(APP, cors_allowed_origins="*")

DB_URI = os.environ["DATABASE_URL"]
APP.config["SQLALCHEMY_DATABASE_URI"] = DB_URI


DB = flask_sqlalchemy.SQLAlchemy(APP)
DB.init_app(APP)
DB.app = APP

DB.session.commit()

import imp_util
import tables
import users
import groups

CLIENTS = []
print(SERVER_PREFIX + "Server started successfully")

################################

#### USERS

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


@APP.route("/new_user", methods=["POST"])
def on_new_user():
    data = flask.request.json
    return create_new_user(data)


@APP.route("/batch_new_users", methods=["POST"])
def bach_new_users():
    data = flask.request.json
    for person in data:
        imp_util.connections.on_new_connection(person)
    return {"success": True}


#### Given info from a user input, changes info of user on database
@APP.route("/edit_user", methods=["POST"])
def on_edit():
    data = flask.request.json
    return imp_util.users.edit_user(data)


#### Given an email, returns a dictionary with the data of the user with such an email
@APP.route("/get_user", methods=["POST"])
def get_user():
    query_user_email = flask.request.json
    return imp_util.users.get_user(query_user_email["email"])


#### GROUPS

#### Makes new group given name and user email


@APP.route("/new_group", methods=["POST"])
def new_group():
    data = flask.request.json
    return imp_util.groups.new_group(data["group_name"], data["emails"])


#### Given a group name, returns a list of users in the group
@APP.route("/get_users", methods=["POST"])
def get_users_list():
    query_name = flask.request.json
    return imp_util.groups.get_users(query_name["group_name"])


#### Given a group name, returns a list of groups a user is in
@APP.route("/get_groups", methods=["POST"])
def get_user_groups_list():
    query_email = flask.request.json
    return imp_util.groups.get_groups(query_email["email"])


#### CONNECTIONS


@APP.route("/upload_doc", methods=["POST"])
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
@APP.route("/new_connection", methods=["POST"])
def on_new_connection():
    data = flask.request.json
    return imp_util.connections.on_new_connection(data)


#### Given 2 user emails,
#### remove the exisiting connection between them if it exists.
#### Returns -1 if such a connection does not exist,
#### and 0 if the connection existed and was deleted.
@APP.route("/delete_connection", methods=["POST"])
def on_delete_connection():
    data = flask.request.json
    return imp_util.connections.on_delete_connection(data)


#### Given a user X's email, returns a list of users X has a connection with.
#### Specifically, it returns a list of dictionaries
#### where each dictionary is the data of a user X has a connection with.
#### Used to query for all connections involving a given user.
@APP.route("/query_connections", methods=["POST"])
def on_query_connections():
    data = flask.request.json
    return {
        "success": True,
        "connections": imp_util.connections.on_query_connections(data),
    }


#### creates a new notification meant for data["email"] with various related fields required
#### title and description are meant to store what to display in the notifications tab
#### type is the type of notifcation, which will specfiy how
#### to handle the notification during various stages (see notifications.py for types)
#### data1-data4 are generic string variables meant for storing data related to the notification
@APP.route("/new_notification", methods=["POST"])
def on_new_notification():
    data = flask.request.json
    notification_data = {data["data1"], data["data2"], data["data3"], data["data4"]}
    return {
        "success": True,
        "response": imp_util.notifications.new_notification(
            data["email"],
            data["titl"],
            data["desc"],
            data["type"],
            notification_data,
        ),
    }


@APP.route("/group_share_contact", methods=["POST"])
def on_group__share_contact():
    data = flask.request.json


@APP.route("/get_nearby_users")
def get_nearby_users():
    data = flask.request.json
    latitude = data["latitude"]
    longitude = data["longitude"]
    email = data["email"]
    # Fetch all nearby users
    # Add current user to nearby users
    # Return nearby users
    return []


@APP.route("/linkedin_login", methods=["POST"])
def on_linkedin_login():
    data = flask.request.json
    access_token = imp_util.linkedin.get_access_token(
        data["authorization_token"]["authentication_code"]
    )
    # get user info
    profile_info = imp_util.linkedin.get_profile(access_token)
    # get email
    email = imp_util.linkedin.get_user_email(access_token)
    # add to db
    profile_info["email"] = email
    return create_new_user(profile_info)


@APP.route("/")
def index():
    return flask.render_template(
        "index.html",
        pageTitle=PAGE_TITLE,
        pageHeader=PAGE_HEADER,
        developerNames=DEVELOPER_NAMES,
        aboutMe=ABOUT_ME,
        links=LINKS,
        contactInfo=CONTACT_INFO,
    )


if __name__ == "__main__":
    SOCKETIO.run(
        APP,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
