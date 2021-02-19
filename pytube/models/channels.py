from dataclasses import dataclass, field
from typing import Optional, Dict

from .items import Localized, Snippet, Status, Content

 
@dataclass
class ChannelsSnippet(Snippet):
    customUrl: Optional[str] = field(default=None, repr=False)
    defaultLanguage: Optional[str] = field(default=None, repr=False)
    country: Optional[str] = field(default=None, repr=False)

@dataclass
class ChannelContent(Content):
    relatedPlaylists: Optional[Dict] = field(default=None, repr=False)

@dataclass
class ChannelStatistics():
    ...

@dataclass
class ChannelTopic():
    ...

@dataclass
class ChannelBranding():
    ...


@dataclass
class Channels():
    snippet: Optional[ChannelSnippet] = field(default=None, repr=False)
    content: Optional[ChannelContent] = field(default=None, repr=False)
    statistics: Optional[ChannelStatistics] = field(default=None, repr=False)
    topic: Optional[ChannelTopic] = field(default=None, repr=False)
    status: Optional[Status] = field(default=None, repr=False)
    branding: Optional[ChannelBranding] = field(default=None, repr=False)
    localized: Optional[Localized] = field(default=None, repr=False)