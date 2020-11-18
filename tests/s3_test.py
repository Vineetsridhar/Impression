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
        self.upload_test_params = [
            {
                KEY_ID: 1,
                KEY_INPUT: ["", "dummyFile.txt"],
                KEY_EXPECTED: "Unexpected Exception",
            },
        ]
        
        self.get_user_data_test_params = [
            {
                KEY_ID: 1,
                KEY_INPUT: {"user_email":"testUser@gmail.com", "data":"qr"},
                KEY_EXPECTED: "https://impression-app.s3.amazonaws.com/testUser%40gmail.com/qr.png",
            },
            {
                KEY_ID: 1,
                KEY_INPUT: {"user_email":"testUser@gmail.com", "data":"avatar"},
                KEY_EXPECTED: "https://impression-app.s3.amazonaws.com/testUser%40gmail.com/avatar.png",
            },
        ]
        
    def test_upload(self):
        for test in self.upload_test_params:
            if test[KEY_ID] == 1:
                with mock.patch('boto3.s3.transfer.S3Transfer.upload_file', self.empty_2):
                    try:
                        s3.upload(test[KEY_INPUT[0]], test[KEY_INPUT[1]])
                        response = "Pass"
                    except:
                        response = "Unexpected Exception"
                    expected = test[KEY_EXPECTED]
                self.assertEqual(response, expected)
    
    def test_get_user_data(self):
        for test in self.get_user_data_test_params:
            if test[KEY_ID] == 1:
                response = s3.s3_get_user_data(test[KEY_INPUT]["user_email"], test[KEY_INPUT]["data"])
                expected = test[KEY_EXPECTED]
                self.assertEqual(response, expected)

# with mock.patch('AWS.S3.ManagedUpload', self.empty1):

if __name__ == "__main__":
    unittest.main()
