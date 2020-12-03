# pylint: disable=missing-function-docstring
# pylint: disable=no-member
# pylint: disable=missing-module-docstring
# pylint: disable=unused-import

import flask_sqlalchemy
from sqlalchemy import desc
from server import DB
import tables
import imp_util

# From https://stackoverflow.com/questions/1958219/convert-sqlalchemy-row-object-to-python-dict
def row2dict(row):
    dct = {}
    for column in row.__table__.columns:
        dct[column.name] = (
            str(getattr(row, column.name)) if getattr(row, column.name) else None
        )

    return dct


#### Get list of groups a user is in
def get_groups(email):
    group = DB.session.query(tables.Groups).filter_by(user_email=email).all()
    DB.session.close()
    resp = []
    if not group:
        return {"success": False}
    for each_group in group:
        resp.append(
            {"group_name": each_group.group_name, "group_id": each_group.group_id}
        )
    return {"success": True, "response": resp}


#### Get list of users' emails from a group
def get_users(name):
    group = (
        DB.session.query(tables.Groups, tables.Users)
        .filter_by(group_name=name, user_email=tables.Users.email)
        .all()
    )
    DB.session.close()
    resp = []
    if not group:
        return {"success": False}
    for each_group in group:
        resp.append(row2dict(each_group.Users))
    return {"success": True, "response": resp}


#### Make new group--
#### given name of group and array of emails
def new_group(name, emails):
    group = DB.session.query(tables.Groups).filter_by(group_name=name).all()
    if not group:
        last_id = (
            DB.session.query(tables.Groups)
            .order_by(desc(tables.Groups.group_id))
            .first()
        )
        if not last_id:
            last_id = 0
        else:
            last_id = last_id.group_id
        for each_email in emails:
            DB.session.add(tables.Groups(last_id + 1, name, each_email))
            DB.session.commit()
        DB.session.close()
        return {"success": True}
    DB.session.close()
    return {"success": False}


def group_share_doc(url, groupid):
    group = DB.session.query(tables.Group).filter_by(group_id=id).all()
    members = []
    for member in group:
        members.append(
            DB.session.query(tables.Users).filter_by(email=member.user_email)
        )
    for user in members:
        imp_util.notifications.new_notification(user.email, "New Document From Group", "accept new document shared from your group?", "group_share_doc", [url,"","",""])