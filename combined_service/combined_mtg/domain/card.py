from dataclasses import dataclass


@dataclass
class Card:
    id: str
    name: str
    mana_cost: int
