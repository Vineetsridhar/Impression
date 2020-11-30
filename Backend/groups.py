# pylint: disable=missing-function-docstring
# pylint: disable=no-member
# pylint: disable=missing-module-docstring
# pylint: disable=unused-import

import flask_sqlalchemy
from server import db
import tables

def get_group(name):
    group = db.session.query(tables.Group).filter_by(group_name=name).first()
    db.session.close()
    if not group:
        return {}
    resp = {
        "user_id": group.user_id,
        "group_name": group.group_name,
    }
    return {"success": True, "response": resp}


def new_group(name, email):
    group = db.session.query(tables.Group).filter_by(group_name=name).all()
    if not group:
        db.session.add(
            tables.Group(
                email, name, 
            )
        )
        db.session.commit()
    db.session.close()
    return {"success": True}
