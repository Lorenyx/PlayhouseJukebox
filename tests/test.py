from dataclasses import dataclass

@dataclass
class Obj():
    key1: int = None
    key2: int = None

data = {'key1': 12, 'key2': 45}

obj = Obj(**data)
print(obj)