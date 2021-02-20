from dataclasses import dataclass, field
from typing import ClassVar, Optional, Dict

from .items import Base

 
@dataclass
class Channels(Base):
    kind: ClassVar[str] = "youtube#channel"

    id: Optional[str] = field(default=None, repr=False)
    snippet: Optional[Dict] = field(default=None, repr=False)
    contentDetails: Optional[Dict] = field(default=None, repr=False)
    statistics: Optional[Dict] = field(default=None, repr=False)
    topicDetails: Optional[Dict] = field(default=None, repr=False)
    status: Optional[Dict] = field(default=None, repr=False)
    brandingSettings: Optional[Dict] = field(default=None, repr=False)
    localized: Optional[Dict] = field(default=None, repr=False)

    def __str__(self):
        return f"{self.kind}(title={self.snippet['title']:!r}, id={self.id})"

