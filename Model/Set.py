from dataclasses import dataclass
from typing import List

from Model.Piece import Piece


@dataclass
class Set:
    id: str
    name: str
    setNumber: str
    pieces: List[Piece]
    totalPieces: int
