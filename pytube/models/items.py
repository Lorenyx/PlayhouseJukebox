from dataclasses import dataclass, field
from typing import Optional, Dict


@dataclass
class Base():
    ...

    @classmethod
    def from_json(cls, data: dict):
        data = {k:v for k,v in data.items() if k in cls.__dataclass_fields__.keys()}
        return cls(**data)

        
@dataclass
class Content():
    videoId: Optional[str] = field(default=None, repr=False)
    note: Optional[str] = field(default=None, repr=False)
    videPublishedAt: Optional[str] = field(default=None, repr=False)
    

@dataclass
class Localized():
    title: Optional[str] = field(default=None, repr=False)
    description: Optional[str] = field(default=None, repr=False)

@dataclass
class Status():
    privacyStatus: Optional[str] = field(default=None, repr=False)


@dataclass
class Snippet():
    "Contains overview of data from response"
    publishedAt: Optional[str] = field(default=None, repr=False)
    channelId: Optional[str] = field(default=None, repr=False)
    title: Optional[str] = field(default=None, repr=False)
    description: Optional[str] = field(default=None, repr=False)
    thumbnails: Optional[str] = field(default=None, repr=False)
    localized: Optional[Localized] = field(default=None, repr=False)