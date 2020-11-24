import requests
import os
import json
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "secret.env")
load_dotenv(dotenv_path)

REDIRECT_URI = os.getenv("REDIRECT_URI")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

#### Exchange auth code for access token
def get_access_token(auth_code):
    base_url = "https://www.linkedin.com/oauth/v2/accessToken"
    query = "?grant_type=authorization_code&code=%s&redirect_uri=%s&client_id=%s&client_secret=%s" % (auth_code, REDIRECT_URI, CLIENT_ID, CLIENT_SECRET)
    response = requests.get(base_url + query)
    data = json.loads(response.text)
    return data["access_token"]

#### Getting Profile data of user
def get_profile(access_tok):
    base_url = "https://api.linkedin.com/v2/me?projection=(id,firstName,lastName,profilePicture(displayImage~:playableStreams))"
    response = requests.get(base_url, headers={"Authorization":'Bearer %s' % access_tok})
    data = json.loads(response.text)
    user_info = {
        "given_name": data["firstName"]["localized"]["en_US"],
        "family_name": data["lastName"]["localized"]["en_US"],
        "picture": data["profilePicture"]["displayImage~"]["elements"][1]["identifiers"][0]["identifier"]
    }
    return user_info

#### Getting email of user
def get_user_email(access_tok):
    base_url = "https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))"
    response = requests.get(base_url, headers={"Authorization":'Bearer %s' % access_tok})
    data = json.loads(response.text)
    return data["elements"][0]["handle~"]["emailAddress"]
