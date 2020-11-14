import unittest
import unittest.mock as mock
import sys

sys.path.insert(1, "../")
import pseudoapp
from pseudoapp import app

import pathlib
import boto3
import pyqrcode
import flask
import flask_sqlalchemy
import flask_socketio

KEY_INPUT = "input"
KEY_EXPECTED = "expected"


# class on_get_user_check(unittest.TestCase):

#     def mocked_new_user_json(self):
#         mocked_request = mock.Mock()
#         mocked_json = {
#             "email": "dummy@gmail.com",
#             # "first_name": "John",
#             # "last_name": "Smith",
#             # "organization": "Impression Co",
#             # "descr": "Description",
#             # "user_type": "Type",
#             # "gen_link_1": "link1",
#             # "gen_link_2": "link2",
#             # "gen_link_3": "link3",
#             # "image": "image",
#             # "doc": "doc",
#         }
#         mocked_request.json.return_value = mocked_json
#         return mocked_request
    
#     def setUp(self):
#         self.success_test_params = [
#             {
#                 KEY_EXPECTED:{
#                     "email": "dummy@gmail.com",
#                     "first_name": "John",
#                     "last_name": "Smith",
#                     "organization": "Impression Co",
#                     "descr": "Description",
#                     "user_type": "Type",
#                     "gen_link_1": "link1",
#                     "gen_link_2": "link2",
#                     "gen_link_3": "link3",
#                     "image": "image",
#                     "doc": "doc",
#                 },
#             },
#         ]

#     def test_success(self):
#         for test in self.success_test_params:
#             with mock.patch('query_user_email', True):
#                 response = pseudoapp.get_user1()
#                 expected = test[KEY_EXPECTED]

#             self.assertEqual(response, expected)

class index_check(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_EXPECTED: "Hello World",
            },
        ]

    def test_success(self):
        for test in self.success_test_params:
            response = pseudoapp.index()
            expected = test[KEY_EXPECTED]

            self.assertEqual(response, expected)

if __name__ == '__main__':
    unittest.main()