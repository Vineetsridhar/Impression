import unittest
import unittest.mock as mock
import sys

sys.path.insert(1, "../")
sys.path.insert(1, "/home/ec2-user/environment/project3/Impression/Backend")
sys.path.append('/home/ec2-user/environment/project3/Impression/Backend')
#import pseudoapp

import os
from os.path import join, dirname
from dotenv import load_dotenv
import flask
import flask_sqlalchemy
import flask_socketio

import ImpUtil
import Users
import tables

KEY_INPUT = "input"
KEY_EXPECTED = "expected"

dummyUser = tables.Users(
    "dummy@gmail.com",
    "John",
    "Smith",
    "Impression Co",
    "Description",
    "Type",
    "link1",
    "link2",
    "link3",
    "image",
    "doc",
)
    
#doesn't work yet without the query.filterby section
class MockedUser():

    def __init__(self, email, fname, lname, org, des, utype, gl1, gl2, gl3, im, doc):
        self.email = email
        self.first_name = fname
        self.last_name = lname
        self.organization = org
        self.descr = des
        self.user_type = utype
        self.gen_link_1 = gl1
        self.gen_link_2 = gl2
        self.gen_link_3 = gl3
        self.image = im
        self.doc = doc

class EditUser(unittest.TestCase):
    
    def mocked_user_query_first(self, email):
        mocked_user = mock.Mock()
        mocked_user.first.return_value = dummyUser
        return mocked_user
    
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "dummy@gmail.com",
                KEY_EXPECTED: {
                    "email": "dummy@gmail.com",
                    "first_name": "John",
                    "last_name": "Smith",
                    "organization": "Impression Co",
                    "descr": "Description",
                    "user_type": "Type",
                    "gen_link_1": "link1",
                    "gen_link_2": "link2",
                    "gen_link_3": "link3",
                    "image": "image",
                    "doc": "doc",
                }
            },
        ]

    def test_edit_user_success(self):
        for test in self.success_test_params:
            #TODO: mock 'query.filter.by' for the database
            with mock.patch('sqlalchemy.orm.query.Query.filter_by', self.mocked_user_query_first):
                response = ImpUtil.Users.get_user(test[KEY_INPUT])
                
                expected = test[KEY_EXPECTED]
            
            self.assertDictEqual(response, expected)

if __name__ == '__main__':
    unittest.main()
