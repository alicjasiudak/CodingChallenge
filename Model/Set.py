from dataclasses import dataclass, field
from typing import List

from Model.Piece import Piece


@dataclass
class Set:
    id: str
    name: str
    setNumber: str
    totalPieces: int
    pieces: List[Piece] = field(default_factory=list)

    def __iter__(self):
        return iter(self.pieces)

