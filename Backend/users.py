import flask_sqlalchemy
from server import db
import tables

def new_user(email, fname, lname, des, usertype, gl1, gl2, gl3, im, doc):
    db.session.add(tables.User(email, fname, lname, des, usertype, gl1, gl2, gl3, im, doc));
    db.session.commit();

def edit_user(account):
    user = tables.User.query.filter_by(email=account.email).first()
    user.email = account.email
    user.first_name = account.first_name
    user.last_name = account.last_name
    user.descr = account.descr
    user.user_type = account.user_type
    user.gen_link_1 = account.gen_link_1
    user.gen_link_2 = account.gen_link_2
    user.gen_link_3 = account.gen_link_3
    user.image = account.image
    user.doc = account.doc
    db.session.commit()
