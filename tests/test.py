import os
import pyyoutube
import logging
from dotenv import load_dotenv

load_dotenv()
log = logging.getLogger()

# Set a severity threshold to one above WARN
log.setLevel(logging.DEBUG)
# ID and Secret need for AUTH requests
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
# Used when auth is not required
API_KEY=os.getenv('API_KEY')

 # variable for token
api = pyyoutube.Api(api_key=API_KEY)
api_with_auth = pyyoutube.Api(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

def start_up():
    "Starts up all needed functions"
    # Paste URI below into browser to login
    global TOKEN
    print(api_with_auth.get_authorization_url()[0])
    INPUT_TOKEN =  input('[=] Enter URI: ') # Paste entire URL after authoirzation here
    TOKEN = api_with_auth.exchange_code_to_access_token(authorization_response=INPUT_TOKEN)


#TODO Refresh token every hour
if __name__ == '__main__':
    start_up()
    print(TOKEN)