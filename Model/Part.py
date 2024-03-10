from dataclasses import dataclass
from typing import Optional

@dataclass
class Part:
    designID: str
    material: int | str
    partType: Optional[str] = None
