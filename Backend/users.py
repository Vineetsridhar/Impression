# pylint: disable=missing-function-docstring
# pylint: disable=no-member
# pylint: disable=missing-module-docstring

import flask_sqlalchemy
from server import db
import tables

#### Given an email, returns a dictionary with the data of the user with such an email
def get_user(query_user_email):
    user = db.session.query(tables.Users).filter_by(email=query_user_email).first()
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


def new_user(email, fname, lname, image):
    user = db.session.query(tables.Users).filter_by(email=email).all()
    if not user:
        db.session.add(
            tables.Users(
                email, fname, lname, None, None, None, None, None, None, image, None
            )
        )
        db.session.commit()

def edit_user(account):
    user = tables.Users.query.filter_by(email=account.email).first()
    user.email = account.email
    user.first_name = account.first_name
    user.last_name = account.last_name
    user.organization = account.organization
    user.descr = account.descr
    user.user_type = account.user_type
    user.gen_link_1 = account.gen_link_1
    user.gen_link_2 = account.gen_link_2
    user.gen_link_3 = account.gen_link_3
    user.image = account.image
    user.doc = account.doc
    db.session.commit()