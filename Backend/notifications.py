# pylint: disable=missing-function-docstring
# pylint: disable=no-member
# pylint: disable=missing-module-docstring
# pylint: disable=unused-import

import flask_sqlalchemy
from server import DB
import tables
import imp_util
import sys

#### creates a new notification meant for data["email"] with various related fields required
#### title and description are meant to store what to display in the notifications tab
#### type is the type of notifcation, which will specfiy how
### to handle the notification during various stages (see notifications.py for types)
#### data1-data4 are generic string variables meant for storing data related to the notification
def new_notification(email, titl, desc, type, data):
    try:
        DB.session.add(
            tables.Notifications(
                email, titl, desc, type, data[0], data[1], data[2], data[3]
            )
        )
        DB.session.commit()
        return {"success": True}
    except:
        print("Error: " + sys.exc_info()[0])
        return {"success": False}
    finally:
        DB.session.close()


#### Given a user email, returns all pending notifications of that user
#### as a list of dictionaries
def get_notifications(user_query_email):
    try:
        notifications = (
            DB.session.query(tables.Notifications)
            .filter_by(user_email=user_query_email)
            .all()
        )
        if not notifications:
            return {"success": False, "response": {}}
        response = []
        for notification in notifications:
            response.append(
                {
                    "id": notification.id,
                    "email": notification.email,
                    "title": notification.title,
                    "description": notification.description,
                }
            )
        return response
    except:
        print("Error: " + sys.exc_info()[0])
        return {"success": False}
    finally:
        DB.session.close()


#### resolve
def resolve_notification(not_id, answer):
    try:
        notification = DB.session.query(tables.Notifications).filter_by(id=not_id).first()
        if notification.type == "connection_confirm":
            if answer["accept"] == True:
                imp_util.connections.on_new_connection(
                    {"user1_email": notification.data1, "user2_email": notification.data2}
                )
        DB.session.delete(notification)
        DB.session.commit()
        return {"success": True}
    except:
        print("Error: " + sys.exc_info()[0])
        return {"success": False}
    finally:
        DB.session.close()
