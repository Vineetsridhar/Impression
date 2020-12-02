# pylint: disable=missing-function-docstring
# pylint: disable=no-member
# pylint: disable=missing-module-docstring
# pylint: disable=unused-import

import flask_sqlalchemy
from server import db
import tables
from sqlalchemy import desc
import imp_util

#From https://stackoverflow.com/questions/1958219/convert-sqlalchemy-row-object-to-python-dict
def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name)) if getattr(row, column.name) else None

    return d

#### Get list of groups a user is in
def get_groups(email):
    group = db.session.query(tables.Groups).filter_by(user_email=email).all()
    db.session.close()
    resp = []
    if not group:
        return {"success": False}
    for each_group in group:
        resp.append({"group_name": each_group.group_name, "group_id":each_group.group_id})
    return {"success": True, "response": resp}

#### Get list of users' emails from a group
def get_users(name):
    group = db.session.query(tables.Groups, tables.Users).filter_by(group_name=name, user_email=tables.Users.email).all()
    db.session.close()
    resp = []
    if not group:
        return {"success": False}
    for each_group in group:
        resp.append(row2dict(each_group.Users))
    return {"success": True, "response": resp}

#### Make new group--
#### given name of group and array of emails
def new_group(name, emails):
    group = 0
    # group = db.session.query(tables.Groups).filter_by(group_name=name).all() Commented For testing so I can use the same group name
    if not group:
        last_id = db.session.query(tables.Groups).order_by(desc(tables.Groups.group_id)).first()
        if not last_id:
            last_id = 0
        else:
            last_id = last_id.group_id
        for each_email in emails:
            db.session.add(
                tables.Groups(
                   last_id + 1, name, each_email
                )
            )
            db.session.commit()
        db.session.close()
        return {"success":True}
    db.session.close()
    return {"success": False}

def group_share_doc(url, groupid):
    group = db.session.query(tables.Group).filter_by(group_id=id).all()
    members = []
    for member in group:
        members.append(db.session.query(tables.Users).filter_by(email=member.user_email))
    for user in members:
        imp_util.notifications.new_notification(user.email, "New Document From Group", "accept new document shared from your group?", "group_share_doc", [url,"","",""])
        
def group_contact_doc(groupid, shared_email):
    group = db.session.query(tables.Group).filter_by(group_id=id).all()
    members = []
    for member in group:
        members.append(db.session.query(tables.Users).filter_by(email=member.user_id))
    
    notification_data = {shared_email, "", "", ""}
    for user in members:
        imp_util.notifications.new_notification(
            user.email,
            "User From Your Group shared a contact",
            "accept new document shared from your group?",
            "group_shared_contact",
            notification_data,
        )
        
