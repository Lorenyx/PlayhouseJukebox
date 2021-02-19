import os
from dotenv import load_dotenv

from pytube import api

load_dotenv()

def main():
    # secrets_file='client_secret.json'

    _api_key = os.getenv('API_KEY')
    _secrets_file = os.getenv('SECRETS_FILE')
    youtube = api.API(api_key=_api_key)
    
    request = youtube.list_channel(id='UC_x5XG1OV2P6uZZ5FSM9Ttw')

    response = request.execute()
    snippet = response['items'][0]['snippet']
    from pytube.models.channels import Channels
    print()

if __name__ == "__main__":
    main()