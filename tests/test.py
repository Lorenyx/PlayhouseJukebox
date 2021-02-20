from dataclasses import dataclass, field
from typing import List, Optional

import dataclasses as ds

@dataclass
class Parent():
    __slots__ = ['key1',]
    key1: int

    def fun(self):
        return 'I am'


@dataclass
class Child(Parent):
    key1: int
    key2: int

    def fun(self):
        print(super().fun() + ' iron man.')

p = Parent(11)
c = Child(12, 45)

print(c.__dir__())
