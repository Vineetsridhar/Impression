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

#### Getting email of user
