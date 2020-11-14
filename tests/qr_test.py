import unittest
import unittest.mock as mock
import sys

# sys.path.insert(1, "../")
sys.path.insert(1, "/home/ec2-user/environment/project3/Impression/Backend")
sys.path.append("/home/ec2-user/environment/project3/Impression/Backend")

import tables
import qr
import s3

import os
import pathlib

import pyqrcode
import flask_sqlalchemy

KEY_ID = ""
KEY_INPUT = "input"
KEY_EXPECTED = "expected"

class qr_tests(unittest.TestCase):
    
    def empty_2(self, val, val2):
        pass
    
    def setUp(self):
        self.create_new_qr_code_test_params = [
            {
                KEY_ID: 1,
                KEY_INPUT: "dummy@gmail.com",
                KEY_EXPECTED: "Pass",
            },
            {
                KEY_ID: 2,
                KEY_INPUT: None,
                KEY_EXPECTED: "Expected Exception",
            },
        ]
        
    def test_on_new_connection(self):
        for test in self.create_new_qr_code_test_params:
            if test[KEY_ID] == 1:
                with mock.patch('s3.upload', self.empty_2):
                    try:
                        qr.create_new_qr_code(test[KEY_INPUT])
                        response = "Pass"
                    except:
                        response = "Unexpected Exception"
                    expected = test[KEY_EXPECTED]
                self.assertEqual(response, expected)
        if test[KEY_ID] == 2:
                with mock.patch('s3.upload', self.empty_2):
                    try:
                        qr.create_new_qr_code(test[KEY_INPUT])
                        response = "Pass"
                    except:
                        response = "Expected Exception"
                    expected = test[KEY_EXPECTED]
                self.assertEqual(response, expected)

# with mock.patch('AWS.S3.ManagedUpload', self.empty1):

if __name__ == "__main__":
    unittest.main()
