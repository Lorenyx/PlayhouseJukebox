from dataclasses import InitVar, dataclass, field
from typing import List, Optional, Dict

import dataclasses as ds


@dataclass
class Base():
    ... 
    @classmethod
    def from_response(cls, data: dict):
        "Returns a cls object made from the data provided"
        data = {k:v for k,v in data.items() if k in cls.__slots__}
        return cls(**data)
