# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=unused-import

import os
import pathlib

import flask_sqlalchemy
import pyqrcode

from server import db
import tables
import s3

################

WORKING_DIR = pathlib.Path(__file__).parent.absolute()

#### Generates a qr code with the given email
#### and stores it in the S3 bucket
def create_new_qr_code(user_email):
    qr_text = "impression://" + user_email
    filename = str(WORKING_DIR) + "/temp/QR_" + user_email + ".png"

    qr_code = pyqrcode.create(qr_text)
    qr_code.png(
        filename, scale=5, module_color=[0, 0, 0, 128], background=[0xFF, 0xFF, 0xFF]
    )
    s3.upload(filename, user_email + "/qr.png")
    os.remove(filename)
