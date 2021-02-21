from dataclasses import dataclass, field
from typing import ClassVar, Optional, List, Dict
from pytube.models.items import Base 


@dataclass
class PytubeIter(Base):
    "An Iterable of videos within a playlist or playlists within a channel"
    kind: Optional[str] = field(default=None)

    items: Optional[List] = field(default=None)
    nextPageToken: Optional[str] = field(default=None, repr=False)
    prevPageToken: Optional[str] = field(default=None, repr=False)
    pageInfo: Optional[Dict] = field(default=None, repr=False) # Dict of totalResults, and resultsPerPage
    items: Optional[List] = field(default=None, repr=False)

    def __str__(self):
        return f"{self.kind}[items={len(self.items)}]"

    def __iter__(self):
        "Returns generator object for yielding"
        index = 0
        while index < self.pageInfo['resultsPerPage']:
            try:
                yield self.items[index]
                index+=1
            except IndexError:
                break
        yield None


    def to_id_list(self):
        it = iter(self)
        return [item['id'] for item in it]
