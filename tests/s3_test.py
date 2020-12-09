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
    
    def mocked_upload(self, filename, key):
        pass
    
    def empty_1(self, val):
        pass
    
    def empty_2(self, val, val2):
        pass
    
    def empty_3(self, val, val2, val3):
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
        
        self.upload_pdf_test_params = [
            {
                KEY_ID: 1,
                KEY_INPUT: {"user_email":"testUser@gmail.com", "data":"qr"},
                KEY_EXPECTED: None,
            },
        ]
        
        self.upload_group_pdf_test_params = [
            {
                KEY_ID: 1,
                KEY_INPUT: {"groupid": "1234", "filename": "group_1234/test.pdf"},
                KEY_EXPECTED: {"success": True},
            },
            {
                KEY_ID: 2,
                KEY_INPUT: {"groupid": None, "filename": 0},
                KEY_EXPECTED: {"success": False},
            },
        ]
        
        self.get_groupdocs_test_params = [
            {
                KEY_ID: 1,
                KEY_INPUT: {"groupid": "1234"},
                KEY_EXPECTED: {"success": True, "response": []},
            },
            {
                KEY_ID: 2,
                KEY_INPUT: {"groupid": None},
                KEY_EXPECTED: {"success": False},
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
    
    def test_upload_pdf(self):
        for test in self.upload_pdf_test_params:
            with mock.patch('boto3.s3.transfer.S3Transfer.upload_file', self.empty_2):
                with mock.patch('s3.upload', self.mocked_upload):
                    with mock.patch('os.remove', self.empty_1):
                        if test[KEY_ID] == 1:
                            response = s3.upload_pdf(test[KEY_INPUT]["user_email"])
                            expected = test[KEY_EXPECTED]
                            self.assertEqual(response, expected)
                            
    def test_upload_group_pdf(self):
        for test in self.upload_group_pdf_test_params:
            with mock.patch('boto3.s3.transfer.S3Transfer.upload_file', self.empty_2):
                with mock.patch('s3.upload', self.mocked_upload):
                    with mock.patch('os.remove', self.empty_1):
                        if test[KEY_ID] == 1:
                            response = s3.upload_group_pdf(test[KEY_INPUT]["groupid"], test[KEY_INPUT]["filename"])
                            expected = test[KEY_EXPECTED]
                            self.assertEqual(response, expected)
                        elif test[KEY_ID] == 2:
                            response = s3.upload_group_pdf(test[KEY_INPUT]["groupid"], test[KEY_INPUT]["filename"])
                            expected = test[KEY_EXPECTED]
                            self.assertEqual(response, expected)
                            
    def test_get_groupdocs(self):
        for test in self.get_groupdocs_test_params:
            if test[KEY_ID] == 1:
                response = s3.get_groupdocs(test[KEY_INPUT]["groupid"])
                expected = test[KEY_EXPECTED]
                self.assertEqual(response, expected)
            elif test[KEY_ID] == 2:
                try:
                    response = s3.get_groupdocs(test[KEY_INPUT]["groupid"])
                except:
                    response = "ValueError"
                expected = test[KEY_EXPECTED]
                self.assertEqual(response, expected)
                    
            
    

# with mock.patch('AWS.S3.ManagedUpload', self.empty1):

if __name__ == "__main__":
    unittest.main()
