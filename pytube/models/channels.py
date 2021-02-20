from dataclasses import dataclass, field
from typing import Optional, Dict

from .items import Localized, Snippet, Status, Content, Base

 
@dataclass
class ChannelsSnippet(Snippet):
    customUrl: Optional[str] = field(default=None, repr=False)
    defaultLanguage: Optional[str] = field(default=None, repr=False)
    country: Optional[str] = field(default=None, repr=False)

@dataclass
class ChannelsContent(Content):
    relatedPlaylists: Optional[Dict] = field(default=None, repr=False)

@dataclass
class ChannelsStatistics():
    ...

@dataclass
class ChannelsTopic():
    ...

@dataclass
class ChannelsBranding():
    ...


@dataclass
class Channels(Base):
    snippet: Optional[ChannelsSnippet] = field(default=None, repr=False)
    content: Optional[ChannelsContent] = field(default=None, repr=False)
    statistics: Optional[ChannelsStatistics] = field(default=None, repr=False)
    topic: Optional[ChannelsTopic] = field(default=None, repr=False)
    status: Optional[Status] = field(default=None, repr=False)
    branding: Optional[ChannelsBranding] = field(default=None, repr=False)
    localized: Optional[Localized] = field(default=None, repr=False)

    
    def __str__(self):
        return f"Channel(snippet={self.snippet}, content={self.content})"


    @staticmethod
    def from_response(self, response):
        "Returns Channels obj from a GET json body"
        # Makes sure that provided data has
        if response['kind'] != 'youtube#channelListResponse':
            return None 

        