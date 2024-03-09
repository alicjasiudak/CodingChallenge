from dataclasses import dataclass, field
from typing import Optional, List

from Model.Variant import Variant


@dataclass
class User:
    id: str
    username: str
    location: str
    brickCount: int
    collection: List[Variant] = field(default_factory=list)
