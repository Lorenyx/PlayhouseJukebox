import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from dataclasses import InitVar, dataclass
from typing import ClassVar, Optional, List, Dict

from .utils.constants import API_SERVICE_NAME, API_VERSION, DEFAULT_QUOTA, COSTS
from .utils.pytube_iter import PytubeIter
from .models.channels import Channels


@dataclass
class API:
    "Main instance of the API class"

    secrets_file: InitVar[str] = None
    api_key: InitVar[str] = None
    token: Optional[str] = None
    quota: Optional[int] = DEFAULT_QUOTA
    
    scopes = [
        "https://www.googleapis.com/auth/youtube",
        "https://www.googleapis.com/auth/userinfo.profile",
    ]


    def __post_init__(self, secrets_file, api_key):
        if secrets_file:
            self.oauth_logon(secrets_file)
        elif api_key:
            self.token = googleapiclient.discovery.build(
            API_SERVICE_NAME, API_VERSION, developerKey=api_key)
        

    def oauth_logon(self, secrets_file):
        "Returns build with OAUTH permissions"
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        secrets_file, self.scopes)
        credentials = flow.run_console()
        self.token = googleapiclient.discovery.build(
            API_SERVICE_NAME, API_VERSION, credentials=credentials)


    def list_channel(self, *, 
        id: str = None,
        forUsername: str = None,
        mine: bool = False,
        part: str = "snippet,contentDetails,statistics" ) -> List:
        "Returns list of Channels that matches args"

        self.quota -= COSTS['list']

        if mine:
            request = self.token.channels().list(part=part, mine=mine)
        else:
            request = self.token.channels().list(
                    part=part,
                    id=id,
                    forUsername=forUsername,
            )

        response = request.execute()
        if 'items' in response:
            return response['items']

        
    def list_playlists( self,  channelId: str, *,
        mine: bool = None,
        part: str = "snippet,contentDetails",
        maxResults: int = 25,
        pageToken: str = None) -> Dict:
        "Returns tuple of ( list(items), [nextPageToken, [prevPageToken]] ) of playlist that belong to a channel"
        self.quota -= COSTS['list']

        if mine:
            request = self.token.playlists().list(
                    part=part,
                    maxResults=maxResults,
                    mine=mine,
                    pageToken=pageToken
            )
        elif id:
            request = self.token.playlists().list(
                    part=part,
                    maxResults=maxResults,
                    channelId=channelId,
                    pageToken=pageToken
            )
        response = request.execute()
        #TODO return PytuberIter instead
        return {k:v for k,v in response.items() if k in ['items', 'nextPageToken', 'prevPageToken']}


    def find_channel( self, *, 
        id: str = None,
        forUsername: str = None,
        mine: bool = False,
        part: str = "snippet,contentDetails,statistics") -> Channels:
        "Returns first Channel that matches args"

        items = self.list_channel(
            id=id, 
            forUsername=forUsername,
            mine=mine,
            part=part
        )
        if items:
            return Channels.from_response(items[0])


    def find_id_playlistitem(self, playlistId: str, videoId: str):
        "returns id of specific video in playlist"
        self.quota -= COSTS['list']

        request = self.token.playlistItems().list(
            part='snippet,contentDetails',
            playlistId=playlistId,
            videoId=videoId
        )
        response = request.execute()
        return response['items'][0]['id']


    def list_playlistitems(self, playlistId: str, *,
        maxResults: int = 25,
        pageToken: str = None):
        "Returns list of videos in a playlist"
        self.quota -= COSTS['list']

        request = self.token.playlistItems().list(
                part='snippet,contentDetails',
                maxResults=maxResults,
                playlistId=playlistId,
                pageToken=pageToken
            )
        response = request.execute()
        return PytubeIter.from_response(response)
        

    def insert_playlistitem( self, playlistId:Optional[str], videoId:Optional[str], 
        *, position:Optional[int] = 0):
        "Adds a Video to the specified Playlist"
        self.quota -= COSTS['insert']

        request = self.token.playlistItems().insert(
            part = "snippet",
            body = {
                "snippet": {
                    "playlistId": playlistId,
                    "position": position,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": videoId
                    }
                }
            }
        )
        response = request.execute()
        return response


    def remove_playlistitem(self, playlistId: str, *,
        videoId: str = None,
        playlistItemId: str = None):
        "Removes video from sepcific playlist, specifiy video id OR playlistItemId"
        self.quota -= COSTS['delete']

        if videoId:
            playlistItemId = self.find_id_playlistitem(playlistId, videoId)
        request = self.token.playlistItems().delete(
            id=playlistItemId
        )
        response = request.execute()
        return response  


    def create_playlist(self, title: str, *,
        description: str = 'This is a playlist of songs posted in a Discord channel.',
        tags: List = None,
        status: str = 'public'):
        "Creates a playlist, privacy defaults to public"

        self.quota -= COSTS['insert']

        request = self.token.playlists().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": title,
                    "description": description,
                    "tags": tags,
                    "defaultLanguage": "en"
                },
                "status": {
                    "privacyStatus": status
                }
            }
        )

        response = request.execute()
        return response


    def update_playlist(self, id: str, *,
        title: str = None, 
        description: str = None,
        tags: List = None,
        status: str = None):
        "Updates a playlist with provided args"

        self.quota -= COSTS['insert']

        request = self.token.playlists().update(
            part="snippet,status",
            body={
                "id": id,
                "snippet": {
                    "title": title,
                    "description": description,
                    "tags": tags,
                    "defaultLanguage": "en"
                },
                "status": {
                    "privacyStatus": status
                }
            }
        )

        response = request.execute()
        return response


    def insert_playlist(self, playlistId: str, sourceId: str, *,
        position: int = 0 ):
        "Inserts a playlist (sourceId) into another playlist (playlistId)"
        # self.quota -= COSTS['insert']
        #TODO insert playlist into playlist
        pyiter = self.list_playlistitems(sourceId)
        videoIds = pyiter.to_id_list()
        for videoId in videoIds:
            self.insert_playlistitem(playlistId, videoId)

        return 0


    @staticmethod
    def parse_url(url: str):
        "Takes a youtube link and returns the ID"
        #TODO parse URLS
        # https://www.youtube.com/watch?v=KoU-s08g5Hc
        # https://youtu.be/KoU-s08g5Hc
        # https://youtu.be/KoU-s08g5Hc?t=55
        # https://www.youtube.com/playlist?list=PLY0iZoD0iOqou8YGz9uaLzHlgdGbL9-El
        # https://www.youtube.com/watch?v=0OmfowGG-AM&list=PLY0iZoD0iOqou8YGz9uaLzHlgdGbL9-El&index=2
        ...