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
        "group_name": group.group_name,
        "user1_email": group.user1_email,
        "user2_email": group.user2_email,
        "user3_email": group.user3_email,
        "user4_email": group.user4_email,
        "user5_email": group.user5_email,
    }
    return resp

def new_group(gr_name, usem1, usem2):
    group = db.session.query(tables.Group).filter_by(group_name=gr_name).all()
    if not group:
        db.session.add(
            tables.Group(
                gr_name, usem1, usem2, None, None, None
            )
        )
        db.session.commit()
    db.session.close()