from dataclasses import dataclass, field
from typing import Optional, List

from .items import Snippet, Status, Content


@dataclass
class PlaylistItem():
    "A specfic video in a playlist"
    snippet: Optional[PlaylistItemSnippet] = field(default=None, repr=False)
    status: Optional[PlaylistItemStatus] = field(default=None, repr=False)
    content: Optional[PlaylistItemContent] = field(default=None, repr=False)


@dataclass
class PlalistItemSnippet(Snippet):
    ...

@dataclass
class PlalistItemStatus(Status):
    ...

@dataclass
class PlalistItemContent(Content):
    ...