# pylint: disable=missing-function-docstring
# pylint: disable=no-member
# pylint: disable=missing-module-docstring
# pylint: disable=unused-import

import flask_sqlalchemy
from server import db
import tables
import imp_util

def new_notification(email, titl, desc, type, data):
    db.session.add(
        tables.Notifications(
            email, titl, desc, type, data[0], data[1], data[2], data[3]
        )
    )
    db.session.commit()
    db.session.close()
    return {"success": True}


#### Given a user email, returns all pending notifications of that user
#### as a list of dictionaries
def get_notifications(user_query_email):
    notifications = db.session.query(tables.Notifications).filter_by(user_email=user_query_email).all()
    db.session.close()
    if not notifications:
        return {"success": False, "response": {}}
    response = []
    for notification in notifications:
        response.append({"id": notification.id, "email": notification.email, "title": notification.title, "description": notification.description})
    return {"success": True, "response": response}


def resolve_notification(not_id, answer, data):
    notification = db.session.query(tables.Notifications).filter_by(id=not_id).first()
    if notification.type == "connection_confirm":
        if answer["accept"] == True:
            imp_util.connections.on_new_connection({"user1_email": notification.data1, "user2_email": notification.data2})
    db.session.delete(notification)
    db.session.commit()
    db.session.close()
    return {"success": True}