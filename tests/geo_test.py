# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-import
# pylint: disable=no-self-use
# pylint: disable=wrong-import-position

import unittest
import unittest.mock as mock
import sys

import os
import pathlib

import flask_sqlalchemy

# sys.path.insert(1, "../")
sys.path.insert(1, "/home/ec2-user/environment/project3/Impression/Backend")
sys.path.append("/home/ec2-user/environment/project3/Impression/Backend")

import tables
import geo
import imp_util

KEY_ID = ""
KEY_INPUT = "input"
KEY_EXPECTED = "expected"

class dummy_geoUser:
    def __init__(self, email, la, lo):
        self.email = email
        self.latitude = la
        self.longitude = lo

class QrTests(unittest.TestCase):
        
    def empty_1(self, val):
        pass
    
    def mocked_db_query(self, val, val2):
        mocked_query = mock.Mock()
        mocked_query.first.return_value = {"email": "dummy@gmail.com", "latitude": 69.9999, "longitude": 69.9999}
        return mocked_query
        
    def mocked_db_query_2(self):
        return dummy_geoUser("dummy@gmail.com", 70.0, 70.0)
        
    def mocked_db_query_3(self):
        return [dummy_geoUser("dummy2@gmail.com", 70.01, 70.01)]
        
    def mocked_db_query_4(self, val):
        return {"email": "dummy@gmail.com"}
        
    def mocked_db_query_5(self, val):
        return 5
        
    def error(self):
        raise Exception
    
    def setUp(self):
        self.add_geo_test_params = [
            {
                KEY_ID: 1,
                KEY_INPUT: {"email": "dummy@gmail.com", "lat": 69.9999, "lon": 69.9999},
                KEY_EXPECTED: None,
            },
            {
                KEY_ID: 2,
                KEY_INPUT: {"email": "dummy2@gmail.com", "lat": 0.0, "lon": 0.0},
                KEY_EXPECTED: None,
            },
            {
                KEY_ID: 3,
                KEY_INPUT: {"email": None, "lat": 69.9999, "lon": 69.9999},
                KEY_EXPECTED: None,
            },
            {
                KEY_ID: 4,
                KEY_INPUT: {"email": None, "lat": 69.9999, "lon": 69.9999},
                KEY_EXPECTED: None,
            },
            {
                KEY_ID: 5,
                KEY_INPUT: {"email": None, "lat": "", "lon": None},
                KEY_EXPECTED: None,
            },
        ]
        self.query_nearby_test_params = [
            {
                KEY_ID: 1,
                KEY_INPUT: {"email": "dummy@gmail.com"},
                KEY_EXPECTED: {'data': []},
            },
            {
                KEY_ID: 1,
                KEY_INPUT: {"email": "dummy2@gmail.com"},
                KEY_EXPECTED: {'data': [{"email": "dummy@gmail.com"}]},
            },
        ]
    
    def test_on_new_connection(self):
        for test in self.add_geo_test_params:
            if test[KEY_ID] == 1:
                with mock.patch("sqlalchemy.orm.session.Session.add", self.empty_1):
                    try:
                        response = geo.add_geo(test[KEY_INPUT]["email"],test[KEY_INPUT]["lat"],test[KEY_INPUT]["lon"])
                    except:
                        response = "Unexpected Exception"
                    expected = test[KEY_EXPECTED]
                self.assertEqual(response, expected)
            
            if test[KEY_ID] == 2:
                with mock.patch("sqlalchemy.orm.session.Session.add", self.empty_1):
                    with mock.patch('sqlalchemy.orm.Query.first', self.mocked_db_query_2):
                        try:
                            response = geo.add_geo(test[KEY_INPUT]["email"],test[KEY_INPUT]["lat"],test[KEY_INPUT]["lon"])
                        except:
                            response = "Unexpected Exception"
                        expected = test[KEY_EXPECTED]
                self.assertEqual(response, expected)
            if test[KEY_ID] == 3:
                with mock.patch("sqlalchemy.orm.session.Session.add", self.empty_1):
                    with mock.patch('sqlalchemy.orm.Query.first', self.mocked_db_query_2):
                        try:
                            response = geo.add_geo(test[KEY_INPUT]["email"],test[KEY_INPUT]["lat"],test[KEY_INPUT]["lon"])
                        except:
                            response = "Unexpected Exception"
                        expected = test[KEY_EXPECTED]
                self.assertEqual(response, expected)
            if test[KEY_ID] == 4:
                with mock.patch("sqlalchemy.orm.session.Session.add", self.error):
                    with mock.patch('sqlalchemy.orm.Query.first', self.mocked_db_query_2):
                        try:
                            response = geo.add_geo(test[KEY_INPUT]["email"],test[KEY_INPUT]["lat"],test[KEY_INPUT]["lon"])
                        except:
                            response = "Unexpected Exception"
                        expected = test[KEY_EXPECTED]
                self.assertEqual(response, expected)
            if test[KEY_ID] == 5:
                with mock.patch("sqlalchemy.orm.session.Session.add", self.empty_1):
                    with mock.patch('sqlalchemy.orm.Query.first', self.mocked_db_query_2):
                        try:
                            response = geo.add_geo(test[KEY_INPUT]["email"],test[KEY_INPUT]["lat"],test[KEY_INPUT]["lon"])
                        except:
                            response = "Unexpected Exception"
                        expected = test[KEY_EXPECTED]
                self.assertEqual(response, expected)
                
                
    def test_query_nearby(self):
        for test in self.query_nearby_test_params:
            if test[KEY_ID] == 1:
                with mock.patch("sqlalchemy.orm.session.Session.add", self.empty_1):
                    with mock.patch('sqlalchemy.orm.Query.first', self.mocked_db_query_2):
                        with mock.patch('sqlalchemy.orm.Query.all', self.mocked_db_query_3):
                            with mock.patch('imp_util.users.get_user', self.mocked_db_query_4):
                                response = geo.query_nearby(test[KEY_INPUT]["email"])
                                expected = test[KEY_EXPECTED]
                                self.assertEqual(response, expected)
            if test[KEY_ID] == 2:
                with mock.patch("sqlalchemy.orm.session.Session.add", self.empty_1):
                    with mock.patch('sqlalchemy.orm.Query.first', self.mocked_db_query_2):
                        with mock.patch('sqlalchemy.orm.Query.all', self.mocked_db_query_3):
                            with mock.patch('imp_util.users.get_user', self.mocked_db_query_4):
                                response = geo.query_nearby(test[KEY_INPUT]["email"])
                                expected = test[KEY_EXPECTED]
                                self.assertEqual(response, expected)

if __name__ == "__main__":
    unittest.main()
