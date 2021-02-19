from dataclasses import dataclass, field
from typing import Optional, List

from .items import Localized, Snippet, Status, Content

@dataclass
class Channels():
    snippet: Optional[PlaylistSnippet] = field(default=None, repr=False)
    status: Optional[PlaylistStatus] = field(default=None, repr=False)
    content: Optional[PlaylistContent] = field(default=None, repr=False)
    player: Optional[PlaylistPlayer] = field(default=None, repr=False)
    localized: Optional[PlaylistLocalized] = field(default=None, repr=False)