# pylint: disable=missing-function-docstring
# pylint: disable=no-member
# pylint: disable=missing-module-docstring
# pylint: disable=unused-import

import flask_sqlalchemy
from sqlalchemy import desc
from server import DB
import tables
import imp_util

import math

def add_geo(email, lat, lon):
    user = DB.session.query(tables.geo_loc).filter_by(email=email).first()
    if not user:
        DB.session.add(tables.geo_loc(email,lat,lon))
    else:
        user.latitude = lat
        user.longitude = lon
    DB.session.commit()
    DB.session.close()
    
def query_nearby(query_email):
    geo_users = DB.session.query(tables.geo_loc).all()
    query_user = DB.session.query(tables.geo_loc).filter_by(email=query_email).first()
    
    lat1 = math.radians(query_user.latitude)
    lon1 = math.radians(query_user.longitude)
    
    nearby = []
    for user in geo_users:
        lat2 = math.radians(user.latitude)
        lon2 = math.radians(user.longitude)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = c * 6373.0 # distance is in meters
        if distance <= 150:
            current_user = imp_util.users.get_user(user.email)
            if current_user["email"] != query_email:
                nearby.append(current_user)
    return {"data":nearby}