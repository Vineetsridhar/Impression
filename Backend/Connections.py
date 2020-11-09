import flask_sqlalchemy
from server import db
import tables
from flask_sqlalchemy import _and, _or

#### Given an email, returns a dictionary with the data of the user with such an email
def get_user(query_user_email):
    user = db.session.query(tables.User).filter(tables.Connection.user_email == query_user_email).first()
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

#### Given 2 user emails, adds them as a new connection to the DB if such a connection does not already exist.
#### Returns -1 if such a connection already exists, and 0 if the connection was added.
def on_new_connection(data):
    for connection in db.session.query(tables.Connection).filter(_and(tables.Connection.user1_email == data["user1_email"], tables.Connection.user2_email == data["user2_email"])).all():
        return -1
    for connection in db.session.query(tables.Connection).filter(_and(tables.Connection.user1_email == data["user2_email"], tables.Connection.user2_email == data["user1_email"])).all():
        return -1
    
    db.session.add(tables.Connection(data["user1_email"], data["user2_email"]))
    db.session.commit()
    return 0

#### Given 2 user emails, remove the exisiting connection between them if it exists.
#### Returns -1 if such a connection does not exist, and 0 if the connection existed and was deleted.
def on_delete_connection(data):
    for connection in db.session.query(tables.Connection).filter(_and(tables.Connection.user1_email == data["user1_email"], tables.Connection.user2_email == data["user2_email"])).all():
        db.session.delete(connection)
        return 0
    for connection in db.session.query(tables.Connection).filter(_and(tables.Connection.user1_email == data["user2_email"], tables.Connection.user2_email == data["user1_email"])).all():
        db.session.delete(connection)
        return 0
    
    return -1

#### Given a user X's email, returns a list of users X has a connection with. Specifically, it returns a list of dictionaries where each dictionary is the data of a user X has a connection with.
#### Used to query for all connections involving a given user.
def on_query_connections(data):
    result = []
    response = []
    
    for connection in db.session.query(tables.Connection).filter(_or(tables.Connection.user1_email == data["user_email"], tables.Connection.user2_email == data["user_email"])).all():
        result.append(connection)

    for connection in result:
        if connection.user1_email == data["user_email"]:
            response.append(get_user(connection.user1_email))
        elif connection.user2_email == data["user_email"]:
            response.append(get_user(connection.user1_email))
    
    return response