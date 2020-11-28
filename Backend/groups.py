# pylint: disable=missing-function-docstring
# pylint: disable=no-member
# pylint: disable=missing-module-docstring
# pylint: disable=unused-import

import flask_sqlalchemy
from server import db
import tables

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
    group = db.session.query(tables.Groups).filter_by(group_name=name).all()
    if not group:
        for each_email in emails:
            db.session.add(
                tables.Group(
                    name, each_email
                )
            )
            db.session.commit()
    db.session.close()
