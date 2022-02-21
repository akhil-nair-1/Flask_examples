import uuid
from dataclasses import dataclass, field


@dataclass
class TestClass:
    _id: str = field(default=uuid.uuid4().hex)


a = TestClass()
b = TestClass()

print(a._id)
print(b._id)