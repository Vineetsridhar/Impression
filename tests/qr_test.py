import unittest
import unittest.mock as mock
import sys

# sys.path.insert(1, "../")
sys.path.insert(1, "/home/ec2-user/environment/project3/Impression/Backend")
sys.path.append("/home/ec2-user/environment/project3/Impression/Backend")

import tables
import s3

import os
import pathlib

import pyqrcode
import flask_sqlalchemy

KEY_INPUT = "input"
KEY_EXPECTED = "expected"

class qr_test(unittest.TestCase):
    
    def empty1(self):
        pass


# with mock.patch('AWS.S3.ManagedUpload', self.empty1):

if __name__ == "__main__":
    unittest.main()
