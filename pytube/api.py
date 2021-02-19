import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from dataclasses import InitVar, dataclass
from typing import Optional, Union, List

from utils import constants

@dataclass
class API:
    "Main instance of the API class"
    secrets_file: InitVar[str] = None
    api_key: InitVar[str] = None
    token: Optional[str] = None
    api_service_name = constants.API_SERVICE_NAME
    api_version = constants.API_VERSION
    DEFAULT_QUOTA = 10000
    scopes = [
        "https://www.googleapis.com/auth/youtube.readonly",
        "https://www.googleapis.com/auth/userinfo.profile",
    ]


    def __post_init__(self, secrets_file, api_key):
        if secrets_file:
            self.oauth_logon(secrets_file)
        elif api_key:
            self.token = googleapiclient.discovery.build(
            self.api_service_name, self.api_version, developerKey=api_key)
        

    def oauth_logon(self, secrets_file):
        "Returns build with OAUTH permissions"
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        secrets_file, self.scopes)
        credentials = flow.run_console()
        self.token = googleapiclient.discovery.build(
            self.api_service_name, self.api_version, credentials=credentials)


    def list_channel(
        self, *, 
        id:Optional[str] = None,
        forUsername:Optional[str] = None,
        mine:Optional[bool] = None
    ):
        if id:
            return self.token.channels().list(
                part="snippet,contentDetails,statistics",
                id=id,
            )
        if forUsername:
            return self.token.channels().list(
                part="snippet,contentDetails,statistics",
                forUsername=forUsername,
            )
        if mine:
            return self.token.channels().list(
                    part="snippet,contentDetails,statistics",
                    mine=mine,
                )