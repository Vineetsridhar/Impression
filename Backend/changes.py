import flask_sqlalchemy
from server import db
import tables

def change_fname(userID, fname):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.first_name = fname
    db.session.commit()
    
def change_lname(userID, lname):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.last_name = lname
    db.session.commit()
    
def change_email(userID, em):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.email = em
    db.session.commit()
    
def change_descr(userID, des):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.descr = des
    db.session.commit()

def change_genlink1(userID, genlink1):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.gen_link_1 = genlink1
    db.session.commit()

def change_genlink2(userID, genlink2):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.gen_link_2 = genlink2
    db.session.commit()

def change_genlink3(userID, genlink3):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.gen_link_3 = genlink3
    db.session.commit()

def change_img(userID, im):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.image = im
    db.session.commit()

def change_doc(userID, document):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.doc = document
    db.session.commit()

def change_type(userID, usertype):
    user = tables.User.query.filter_by(user_id=userID).first()
    user.user_type = usertype
    db.session.commit()