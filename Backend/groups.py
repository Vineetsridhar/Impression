# pylint: disable=missing-function-docstring
# pylint: disable=no-member
# pylint: disable=missing-module-docstring
# pylint: disable=unused-import

import flask_sqlalchemy
from sqlalchemy import desc
from server import DB
import tables
import imp_util
import sys

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
    try:
        group = DB.session.query(tables.Groups).filter_by(user_email=email).all()
        resp = []
        if not group:
            return {"success": False}
        for each_group in group:
            resp.append(
                {"group_name": each_group.group_name, "group_id": each_group.group_id}
            )
        return {"success": True, "response": resp}
    except:
        print("Error: " + sys.exc_info()[0])
        return {"success": False}
    finally:
        DB.session.close()


#### Get list of users' emails from a group
def get_users(name):
    try:
        group = (
            DB.session.query(tables.Groups, tables.Users)
            .filter_by(group_name=name, user_email=tables.Users.email)
            .all()
        )
        resp = []
        if not group:
            return {"success": False}
        for each_group in group:
            resp.append(row2dict(each_group.Users))
        return {"success": True, "response": resp}
    except:
        print("Error: " + sys.exc_info()[0])
        return {"success": False}
    finally:
        DB.session.close()


#### Make new group--
#### given name of group and array of emails
def new_group(name, emails):
    try:
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
        return {"success": False}
    except:
        print("Error: " + sys.exc_info()[0])
        return {"success": False}
    finally:
        DB.session.close()

#### add user to an already existing group
def add_user(name, email):
    try:
        group = (
            DB.session.query(tables.Groups)
            .filter_by(group_name=name)
            .order_by(desc(tables.Groups.group_id))
            .first())
        last_id = group.group_id
        DB.session.add(tables.Groups(last_id, name, email))
        DB.session.commit()
        return {"success": True}
    except:
        print("Error: " + sys.exc_info()[0])
        return {"success": False}
    finally:
        DB.session.close()

    
#### have a user leave a group
def leave_group(g_id, name, email):
    try:
        row = (DB.session.query(tables.Groups)
        .filter_by(group_id=g_id, group_name=name, user_email=email))
        DB.session.delete(row)
        DB.session.commit()
        return {"success": True}
    except:
        print("Error: " + str(sys.exc_info()[0]))
        return {"success": False}
    finally:
        DB.session.close()
