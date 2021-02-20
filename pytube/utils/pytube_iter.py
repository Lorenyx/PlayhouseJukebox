from dataclasses import dataclass, field
from typing import ClassVar, Optional, List, Dict


@dataclass
class PytubeIter(iter):
    "An Iterable of videos within a playlist or playlists within a channel"
    kind: ClassVar[List] = ["youtube#playlistItemListResponse", "youtube#playlistListResponse"]

    items: Optional[List] = field(default=None)
    nextPageToken: Optional[str] = field(default=None, repr=False)
    prevPageToken: Optional[str] = field(default=None, repr=False)
    pageInfo: Optional[Dict] = field(default=None, repr=False) # Dict of totalResults, and resultsPerPage
    items: Optional[List] = field(default=None, repr=False)

    def __str__(self):
        return f"{self.kind}[{self.items}]"
    

    def __iter__(self):
        return self


    def __next__(self):
        "Returns next item in Iter"
        index = 0
        while index < self.pageInfo['maxResults']:
            try:
                yield self.items[index]
                index+=1
            except IndexError:
                break
        if self.nextPageToken:


