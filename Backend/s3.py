# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=inconsistent-return-statements

import os
from os.path import join, dirname
import pathlib
import boto3
from dotenv import load_dotenv


################

SERVER_PREFIX = "\033[96m" + "[SERVER]" + "\033[0m" + " "

dotenv_path = join(dirname(__file__), "secret.env")
load_dotenv(dotenv_path)

WORKING_DIR = pathlib.Path(__file__).parent.absolute()

s3 = boto3.resource(
    service_name="s3",
    region_name=os.environ["AWS_DEFAULT_REGION"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)

################

#### Given a filename and the desired file key,
#### upload filename to S3 bucket
def upload(filename, key):
    s3.Bucket("impression-app").upload_file(Filename=filename, Key=key)
    print(SERVER_PREFIX + "File uploaded to S3: " + filename + " as '" + key + "'")


def upload_pdf(user_email):
    filename = str(WORKING_DIR) + "/temp/resume_" + user_email + ".pdf"
    s3.upload(filename, user_email + "/resume.pdf") 
    os.remove(filename)
    
    
####
def s3_get_user_data(user_email, data):
    if data == "qr":
        return (
            "https://impression-app.s3.amazonaws.com/"
            + user_email.replace("@", "%40")
            + "/qr.png"
        )
    if data == "avatar":
        return (
            "https://impression-app.s3.amazonaws.com/"
            + user_email.replace("@", "%40")
            + "/avatar.png"
        )
