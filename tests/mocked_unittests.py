import unittest
import unittest.mock as mock
import sys

sys.path.insert(1, "../")
# sys.path.insert(1, "../Backend")
import pseudoapp

import os
from os.path import join, dirname
from dotenv import load_dotenv
import flask
import flask_sqlalchemy
import flask_socketio

KEY_INPUT = "input"
KEY_EXPECTED = "expected"

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
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "something@njit.edu",
                KEY_EXPECTED: {
                    "email": "something@njit.edu",
                    "first_name": "FName",
                    "last_name": "LName",
                    "organization": "None",
                    "descr": "None",
                    "user_type": "None",
                    "gen_link_1": "linkedin.com",
                    "gen_link_2": "github.com",
                    "gen_link_3": "None",
                    "image": "someimage.jpg",
                    "doc": "None"
                }
            },
        ]
        
    def mocked_query(self, email):
        return [
            MockedUser(
                "something@njit.edu",
                "FName",
                "LName",
                "None",
                "None",
                "None",
                "linkedin.com",
                "github.com",
                "None",
                "someimage.jpg",
                "None",
            )
        ]

    def test_edit_user_success(self):
        for test in self.success_test_params:
            #TODO: mock 'query.filter.by' for the database
            with mock.patch('Users.query.filter_by', self.mocked_query):
                response = pseudoapp.edit_user(test[KEY_INPUT])
                expected = test[KEY_EXPECTED]
            
            self.assertDictEqual(response, expected)

if __name__ == '__main__':
    unittest.main()
