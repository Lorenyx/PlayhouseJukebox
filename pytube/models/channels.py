from dataclasses import dataclass, field
from typing import ClassVar, Optional, Union, Dict, List

from .items import Localized, Snippet, Status, Content, Base

 
@dataclass
class Channels(Base):
    # Optimizes code, only values in slots are allowed to be fields
    __slots__ = ['snippet', 'contentDetails', 'statistics', 'topic', 'status', 'branding', 'localized',]

    kind: ClassVar[str] = "youtube#channel"

    snippet: Optional[Dict] = field(default=None, repr=False)
    contentDetails: Optional[Dict] = field(default=None, repr=False)
    statistics: Optional[Dict] = field(default=None, repr=False)
    topicDetails: Optional[Dict] = field(default=None, repr=False)
    status: Optional[Dict] = field(default=None, repr=False)
    brandingSettings: Optional[Dict] = field(default=None, repr=False)
    localized: Optional[Dict] = field(default=None, repr=False)

    def __str__(self):
        return f"Channel(snippet={type(self.snippet)}, content={type(self.contentDetails)})"
