import dataclasses as ds

from dataclasses import dataclass
from typing import List


@dataclass
class Base():
    ... 

    @classmethod
    def field_names(cls) -> List:
        "Returns a list of the field names"
        return [f.name for f in ds.fields(cls)]

    @classmethod
    def from_response(cls, data: dict):
        "Returns a cls object made from the data provided"
        data = {k:v for k,v in data.items() if k in cls.field_names()}
        return cls(**data)
