import os
from dotenv import load_dotenv

from pytube.models.channels import Channels
from pytube import api

load_dotenv()

def main():
    # secrets_file='client_secret.json'

    _api_key = os.getenv('API_KEY')
    _secrets_file = os.getenv('SECRETS_FILE')
    youtube = api.API(secrets_file=_secrets_file)
    
    # request = youtube.list_channel(id='UC_x5XG1OV2P6uZZ5FSM9Ttw')

    # response = request.execute()
    # data = response['items'][0]
    # channel = Channels.from_response(data)
    # PlaylistId= PLwJ3OK9IWOt5F18lWIGme-Acq0wiDkSks
    print(youtube.insert_playlist('PLwJ3OK9IWOt5F18lWIGme-Acq0wiDkSks','dQw4w9WgXcQ'))
    

if __name__ == "__main__":
    main()