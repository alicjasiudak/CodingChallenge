from dataclasses import dataclass, field
from typing import Optional, List

from Model.CollectionItem import CollectionItem


@dataclass
class User:
    id: str
    username: str
    location: str
    brickCount: int
    collection: List[CollectionItem] = field(default_factory=list)
