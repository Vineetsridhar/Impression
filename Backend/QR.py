import os
import pathlib

import pyqrcode
import flask_sqlalchemy

from server import db
import tables
import S3

################

WORKING_DIR = pathlib.Path(__file__).parent.absolute()

#### Generates a qr code with the given email
#### and stores it in the S3 bucket
def create_new_qr_code(user_email):
    qrText = "impression://" + user_email
    filename = str(WORKING_DIR) + '/temp/QR_' + user_email + '.png'
    
    qrCode = pyqrcode.create(qrText)
    qrCode.png(filename, scale=5, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    S3.upload(filename, user_email + "/qr.png")
    os.remove(filename)