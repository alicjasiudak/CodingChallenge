from dataclasses import dataclass, field
from typing import Optional, List

from Model.Piece import Piece


@dataclass
class User:
    id: str
    username: str
    location: str
    brickCount: int
    collection: List[Piece] = field(default_factory=list)



