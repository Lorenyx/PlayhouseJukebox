from dataclasses import dataclass, field
from typing import Optional, Dict


@dataclass
class Base():
    ...

    @classmethod
    def from_response(cls, data: dict):
        data = {k:v for k,v in data.items() if k in cls.__dataclass_fields__.keys()}
        return cls(**data)

        
@dataclass
class Content(Base):
    videoId: Optional[str] = field(default=None, repr=False)
    note: Optional[str] = field(default=None, repr=False)
    videPublishedAt: Optional[str] = field(default=None, repr=False)
    
    def __str__(self):
        return f'Content(videoId="{self.videoId}")'

    

@dataclass
class Localized(Base):
    title: Optional[str] = field(default=None, repr=False)
    description: Optional[str] = field(default=None, repr=False)

@dataclass
class Status(Base):
    privacyStatus: Optional[str] = field(default=None, repr=False)

    def __str__(self):
        return f'Status={self.privacyStatus}'


@dataclass
class Snippet(Base):
    "Contains overview of data from response"
    publishedAt: Optional[str] = field(default=None, repr=False)
    channelId: Optional[str] = field(default=None, repr=False)
    title: Optional[str] = field(default=None, repr=False)
    description: Optional[str] = field(default=None, repr=False)
    thumbnails: Optional[str] = field(default=None, repr=False)
    localized: Optional[Localized] = field(default=None, repr=False) 

    def __str__(self):
        return f'Snippet(title="{self.title}, channelId="{self.channelId}")'