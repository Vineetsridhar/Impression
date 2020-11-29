# pylint: disable=missing-function-docstring
# pylint: disable=no-member
# pylint: disable=missing-module-docstring
# pylint: disable=unused-import

import flask_sqlalchemy
from server import db
import tables
from sqlalchemy import desc

#### Get list of groups a user is in
def get_groups(email):
    group = db.session.query(tables.Groups).filter_by(user_email=email).all()
    db.session.close()
    resp = []
    if not group:
        return {"success": False}
    for each_group in group:
        resp.append(each_group.group_name)
    return {"success": True, "response": resp}

#### Get list of users' emails from a group
def get_users(name):
    group = db.session.query(tables.Groups).filter_by(group_name=name).all()
    db.session.close()
    resp = []
    if not group:
        return {"success": False}
    for each_group in group:
        resp.append(each_group.user_email)
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
    return {"success":False}
