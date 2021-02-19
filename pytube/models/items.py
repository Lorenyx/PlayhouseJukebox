from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Snippet():
    "Contains overview of data from response"
    publishedAt: Optional[str] = field(default=None, repr=False)
    channelId: Optional[str] = field(default=None, repr=False)
    title: Optional[str] = field(default=None, repr=False)
    description: Optional[str] = field(default=None, repr=False)
    thumbnails: Optional[str] = field(default=None, repr=False)

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