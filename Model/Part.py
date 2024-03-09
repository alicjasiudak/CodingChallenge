from dataclasses import dataclass


@dataclass
class Part:
    designID: str
    material: int
    partType: str
