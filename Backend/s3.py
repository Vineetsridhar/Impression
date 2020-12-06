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

DOTENV_PATH = join(dirname(__file__), "secret.env")
load_dotenv(DOTENV_PATH)

WORKING_DIR = pathlib.Path(__file__).parent.absolute()

S3 = boto3.resource(
    service_name="s3",
    region_name=os.environ["AWS_DEFAULT_REGION"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)

################

#### Given a filename and the desired file key,
#### upload filename to S3 bucket
def upload(filename, key):
    S3.Bucket("impression-app").upload_file(Filename=filename, Key=key)
    print(SERVER_PREFIX + "File uploaded to S3: " + filename + " as '" + key + "'")


def upload_pdf(user_email):
    filename = str(WORKING_DIR) + "/temp/resume_" + user_email + ".pdf"
    upload(filename, user_email + "/resume.pdf")
    os.remove(filename)


def upload_group_pdf(groupid, fileKey):
    try:
        filePath = str(WORKING_DIR) + "/temp/groupdoc_" + groupid + "_" + fileKey + ".pdf"
        amazonName = "group_" + groupid + "/" + fileKey + ".pdf"
        upload(filePath, amazonName)
        os.remove(filePath)
        return {"success": True}
    except:
        print(SERVER_PREFIX + "Error: failed to upload group doc")
        return {"success": False}
    
    
#### Given a groupid, returns filenames and file URLS of all relevent docs belonging to that group
def get_groupdocs(groupid):
    try:
        conn = boto3.client('s3')  # again assumes boto.cfg setup, assume AWS S3
        docs = []
        for file in conn.list_objects(Bucket='impression-app')['Contents']:
            if file['Key'].split("/")[0] == ("group_" + groupid):
                docs.append({"filename": file['Key'].split("/")[1],"url":"https://impression-app.s3.amazonaws.com/" + file['Key']})
        return {"success": True, "response": docs}
    except:
        print(SERVER_PREFIX + "Error: could not retrieve group documents")
        return {"success": False}
        
    
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