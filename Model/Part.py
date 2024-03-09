from dataclasses import dataclass
from typing import Optional


@dataclass
class Part:
    designID: str
    material: int
    partType: Optional[str] = None
