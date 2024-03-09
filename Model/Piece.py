from dataclasses import dataclass

from Model.Part import Part


@dataclass
class Piece:
    part: Part
    quantity: int
