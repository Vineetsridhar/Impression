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
    "Chris": "I am a senior at NJIT pursing a career in Software Engineering.",
    "Vineet": "I am a 3rd year student at NJIT who has a passion for mobile development",
    "Rami": "Hello! I'm currently a Senior undergraduate at NJIT pursuing a B.S. in Computer Science.",
    "Stephanie": "I'm a senior CS manjor at NJIT, looking for a career in Software Development.",
}

LINKEDIN_LINKS = {
    "Chris": "https://www.linkedin.com/in/chris-mazzei-99a843133/",
    "Vineet": "https://www.linkedin.com/in/vineet-sridhar/",
    "Rami": "https://www.linkedin.com/in/bazoqa/",
    "Stephanie": "https://linkedin.com/in/stephanie-nieve-silva"}
GITHUB_LINKS = {
    "Chris": "https://github.com/ChrisMazzei",
    "Vineet": "https://github.com/vineetsridhar",
    "Rami": "https://github.com/bazoqa",
    "Stephanie": "https://github.com/smn29"}

CONTACT_INFO = {
    "Chris": "Contact Info.",
    "Vineet": "Contact me at https://www.linkedin.com/in/vineet-sridhar/",
    "Rami": "Email: rab63@njit.edu",
    "Stephanie": "Email: smn29@njit.edu",
}

ABOUT_APP = """Due to COVID-19, recruiters and students struggle to find ways to make a
                virtual connection to be as successful as an in-person one; it has
                become an arduous task for recruiters and applicants to exchange
                information. This is where our application, Impression, comes in."""

CREATED_WITH = ["Created with:", "React Native,", "Python,", "Flask,", "PostgreSQL,", "Expo."]
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


#### Given a group name and email, adds user to existing group
@APP.route("/add_user", methods=["POST"])
def add_user():
    data = flask.request.json
    return imp_util.groups.add_user(data["group_name"], data["email"])


#### Given a group id, group name, and email, removes user from group
@APP.route("/leave_group", methods=["POST"])
def leave_group():
    data = flask.request.json
    return imp_util.groups.leave_group(data["group_id"], data["group_name"], data["email"])


@APP.route("/upload_doc", methods=["POST"])
def on_upload_doc():
    form = flask.request.form
    data = flask.request.files["file"]
    data.save("temp/resume_%s.pdf" % form["email"])
    imp_util.s3.upload_pdf(form["email"])
    return {}


#### Form requires groupid and filename
@APP.route("/upload_group_pdf", methods=["POST"])
def on_upload_group_doc():
    try:
        print(SERVER_PREFIX + str(os.listdir()))
        form = flask.request.form
        data = flask.request.files["file"]
        data.save("temp/groupdoc_" + form["groupid"] + "_" + form["filename"])
        return imp_util.s3.upload_group_pdf(form["groupid"], form["filename"])
    except Exception as err:
        print(err)
        return {"success":False}


#### Requires groupid, returns response json with a list of dictionaries that contains filenames and urls of docs
@APP.route("/get_group_docs", methods=["POST"])
def on_get_group_doc():
    data = flask.request.json
    return imp_util.s3.get_groupdocs(data["groupid"])


#### CONNECTIONS

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


@APP.route("/group_share_contact", methods=["POST"])
def on_group__share_contact():
    data = flask.request.json


@APP.route("/get_nearby_users", methods=["POST"])
def get_nearby_users():
    data = flask.request.json
    print(data)
    imp_util.geo.add_geo(data["email"], data["latitude"], data["longitude"])
    return imp_util.geo.query_nearby(data["email"])


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
        aboutApp=ABOUT_APP,
        createdWith=CREATED_WITH,
        aboutMe=ABOUT_ME,
        linkedinLinks=LINKEDIN_LINKS,
        githubLinks=GITHUB_LINKS,
        contactInfo=CONTACT_INFO,
    )


if __name__ == "__main__":
    SOCKETIO.run(
        APP,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
