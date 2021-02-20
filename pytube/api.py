import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from dataclasses import InitVar, dataclass
from typing import ClassVar, Optional, Union, List

from .utils.constants import API_SERVICE_NAME, API_VERSION, DEFAULT_QUOTA
from .models.channels import Channels

@dataclass
class API:
    "Main instance of the API class"

    secrets_file: InitVar[str] = None
    api_key: InitVar[str] = None
    token: Optional[str] = None
    quota: Optional[int] = DEFAULT_QUOTA
    
    scopes = [
        "https://www.googleapis.com/auth/youtube.readonly",
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



    def query_channel(self, *, 
        id: str = None,
        forUsername: str = None,
        mine: bool = None,
        part: str = "snippet,contentDetails,statistics") -> List:
        "Returns list of Channels that matches args"

        COST = 1 # Cost to make channel list request
        self.quota -= COST

        if mine:
            request = self.token.channels().list(
                    part=part,
                    mine=mine,
            )
        elif id:
            request = self.token.channels().list(
                part=part,
                id=id,
            )
        elif forUsername:
            request = self.token.channels().list(
                part=part,
                forUsername=forUsername,
            )

        response = request.execute()
        return response['items']


    def find_channel( self, *, 
        id: str = None,
        forUsername: str = None,
        mine: bool = None,
        part: str = "snippet,contentDetails,statistics"):
        "Returns first Channel that matches args"

        items = self.query_channel(
            id=id, 
            forUsername=forUsername,
            mine=mine,
            part=part
        )
        if items:
            return Channels.from_response(items[0])


    def create_playlist( self, *, 
        title:Optional[str] = None,
        description:Optional[str] = None,
        status:Optional[str] = None, ):
        "Creates the playlist provided under the logged-in account"
