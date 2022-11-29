from abc import ABC, abstractmethod
from typing import List

from mtg.domain.card import Card


class CardsRepository(ABC):
    @abstractmethod
    def find_one(self) -> Card:
        raise NotImplemented

    @abstractmethod
    def get_number_of_items(self, number_of_items) -> List[Card]:
        raise NotImplemented

    @abstractmethod
    def get_one_item_from_position(self, position) -> Card:
        raise NotImplemented
