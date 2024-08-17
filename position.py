from dataclasses import dataclass


@dataclass
class Position:
    x: int | float = 0
    y: int | float = 0
    # z: int = 0
