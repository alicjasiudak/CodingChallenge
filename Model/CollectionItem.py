from dataclasses import dataclass
from typing import List

from Model.Variant import Variant


@dataclass
class CollectionItem:
    pieceId: str
    variants: List[Variant]