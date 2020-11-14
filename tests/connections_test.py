import unittest
import unittest.mock as mock
import sys

sys.path.insert(1, "/home/ec2-user/environment/project3/Impression/Backend")
sys.path.append("/home/ec2-user/environment/project3/Impression/Backend")

import os
from os.path import join, dirname
from dotenv import load_dotenv
import flask
import flask_sqlalchemy
import flask_socketio

import imp_util
import users
import connections
import tables

KEY_ID = 0
KEY_INPUT = "input"
KEY_EXPECTED = "expected"

KEY_EMAIL = "email"
KEY_FNAME = "fname"
KEY_LNAME = "lname"
KEY_IMAGE = "image"

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

class connections_tests(unittest.TestCase):

    def get_mocked_user(self, value):
        return dummyUser
    
    def empty(self):
        pass
    
    def empty_2(self, value):
        pass
    
    def mocked_get_user(self, email):
        return "dummy2@gmail.com"
    
    def mocked_user_query_all(self):
        return ["dummy2@gmail.com"]
        
    def mocked_user_query_all_empty(self):
        return []
        
    def mocked_user_query_all_1(self):
        return [tables.Connections("dummy2@gmail.com", "dummy@gmail.com")]
    
    def mocked_user_query_all_2(self):
        return [tables.Connections("dummy@gmail.com", "dummy2@gmail.com")]
        
    def setUp(self):
        self.on_new_connection_test_params = [
            {
                KEY_ID: 1,
                KEY_INPUT: {
                    "user1_email": "dummy1@gmail.com",
                    "user2_email": "dummy2@gmail.com",
                },
                KEY_EXPECTED: "dummy2@gmail.com"
            },
            {
                KEY_ID: 2,
                KEY_INPUT: {
                    "user1_email": "dummy1@gmail.com",
                    "user2_email": "dummy2@gmail.com",
                },
                KEY_EXPECTED: "dummy2@gmail.com"
            },
            {
                KEY_ID: 3,
                KEY_INPUT: {
                    "user1_email": None,
                    "user2_email": None,
                },
                KEY_EXPECTED: {"success": False}
            },
            {
                KEY_ID: 4,
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
        
        self.on_delete_connection_test_params = [
            {
                KEY_ID: 1,
                KEY_INPUT: {
                    "user1_email": "dummy1@gmail.com",
                    "user2_email": "dummy2@gmail.com",
                },
                KEY_EXPECTED: 0
            },
            {
                KEY_ID: 2,
                KEY_INPUT: {
                    "user1_email": "dummy1@gmail.com",
                    "user2_email": "dummy2@gmail.com",
                },
                KEY_EXPECTED: -1
            },
        ]
        
        self.on_query_connection_test_params = [
            {
                KEY_ID: 1,
                KEY_INPUT: {
                    "user_email": "dummy2@gmail.com",
                },
                KEY_EXPECTED: [self.get_mocked_user(0)]
            },
            {
                KEY_ID: 2,
                KEY_INPUT: {
                    "user_email": "dummy@gmail.com",
                },
                KEY_EXPECTED: [self.get_mocked_user(0)]
            },
            {
                KEY_ID: 3,
                KEY_INPUT: {
                    "": "",
                },
                KEY_EXPECTED: None
            },
        ]
        
    def test_on_new_connection(self):
        for test in self.on_new_connection_test_params:
            
            if test[KEY_ID] == 1:
                with mock.patch('sqlalchemy.orm.query.Query.all', self.mocked_user_query_all):
                    with mock.patch('users.get_user', self.mocked_get_user):
                        with mock.patch('sqlalchemy.orm.session.Session.add', self.empty):
                            response = imp_util.connections.on_new_connection(test[KEY_INPUT])
                            expected = test[KEY_EXPECTED]
        
                self.assertEqual(response, expected)
            
            if test[KEY_ID] == 2:
                with mock.patch('sqlalchemy.orm.query.Query.all', self.mocked_user_query_all_empty):
                    with mock.patch('users.get_user', self.mocked_get_user):
                        with mock.patch('sqlalchemy.orm.session.Session.add', self.empty_2):
                            response = imp_util.connections.on_new_connection(test[KEY_INPUT])
                            expected = test[KEY_EXPECTED]
        
                self.assertEqual(response, expected)
            
            if test[KEY_ID] == 3:
                with mock.patch('sqlalchemy.orm.query.Query.all', self.mocked_user_query_all_empty):
                    with mock.patch('users.get_user', self.empty):
                        with mock.patch('sqlalchemy.orm.session.Session.add', self.empty_2):
                            response = imp_util.connections.on_new_connection(test[KEY_INPUT])
                            expected = test[KEY_EXPECTED]
        
                self.assertEqual(response, expected)
                
    def test_delete_connection(self):
        for test in self.on_delete_connection_test_params:
            
            if test[KEY_ID] == 1:
                with mock.patch('sqlalchemy.orm.query.Query.all', self.mocked_user_query_all):
                    with mock.patch('users.get_user', self.mocked_get_user):
                        with mock.patch('sqlalchemy.orm.session.Session.delete', self.empty_2):
                            with mock.patch('sqlalchemy.orm.session.Session.add', self.empty):
                                response = imp_util.connections.on_delete_connection(test[KEY_INPUT])
                                expected = test[KEY_EXPECTED]
        
                self.assertEqual(response, expected)
            
            if test[KEY_ID] == 2:
                with mock.patch('sqlalchemy.orm.query.Query.all', self.mocked_user_query_all_empty):
                    with mock.patch('users.get_user', self.mocked_get_user):
                        with mock.patch('sqlalchemy.orm.session.Session.delete', self.empty):
                            with mock.patch('sqlalchemy.orm.session.Session.add', self.empty):
                                response = imp_util.connections.on_delete_connection(test[KEY_INPUT])
                                expected = test[KEY_EXPECTED]
            
                self.assertEqual(response, expected)
    
    def test_query_connection(self):
        for test in self.on_query_connection_test_params:
            
            if test[KEY_ID] == 1:
                with mock.patch('sqlalchemy.orm.query.Query.all', self.mocked_user_query_all_1):
                    with mock.patch('users.get_user', self.get_mocked_user):
                        response = imp_util.connections.on_query_connections(test[KEY_INPUT])
                        expected = test[KEY_EXPECTED]
        
                self.assertEqual(response, expected)
                
            if test[KEY_ID] == 2:
                with mock.patch('sqlalchemy.orm.query.Query.all', self.mocked_user_query_all_1):
                    with mock.patch('users.get_user', self.get_mocked_user):
                        response = imp_util.connections.on_query_connections(test[KEY_INPUT])
                        expected = test[KEY_EXPECTED]
        
                self.assertEqual(response, expected)
                
            if test[KEY_ID] == 3:
                with mock.patch('sqlalchemy.orm.query.Query.all', self.mocked_user_query_all_1):
                    with mock.patch('users.get_user', self.get_mocked_user):
                        response = imp_util.connections.on_query_connections(test[KEY_INPUT])
                        expected = test[KEY_EXPECTED]
        
                self.assertEqual(response, expected)

###############################################################

if __name__ == '__main__':
    unittest.main()
