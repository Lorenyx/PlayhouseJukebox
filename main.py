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
    # PlistId = PLwJ3OK9IWOt5F18lWIGme-Acq0wiDkSks
    # VideoId = dQw4w9WgXcQ
    # NynanPlist = PLY0iZoD0iOqou8YGz9uaLzHlgdGbL9-El
    tmp = youtube.insert_playlist('PLwJ3OK9IWOt5F18lWIGme-Acq0wiDkSks', 'PLY0iZoD0iOqou8YGz9uaLzHlgdGbL9-El')
    print(tmp)

    

if __name__ == "__main__":
    main()