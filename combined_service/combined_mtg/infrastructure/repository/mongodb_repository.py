from typing import List

from pymongo import MongoClient

from combined_mtg.domain.card import Card
from combined_mtg.infrastructure.repository.repository import CardsRepository
from combined_mtg.config import (
    MONGO_HOST, MONGO_PORT, MONGO_TIMEOUT, MONGO_USERNAME, MONGO_PASSWORD
)


class MongodbRepository(CardsRepository):
    def __init__(self) -> None:
        self.client: MongoClient = MongoClient(
            host=f"{MONGO_HOST}:{MONGO_PORT}",
            serverSelectionTimeoutMS=MONGO_TIMEOUT,
            username=MONGO_USERNAME,
            password=MONGO_PASSWORD,
        )
        self.cards = self.client["cards"]

    def find_one(self) -> Card:
        try:
            collection = self.cards.list_of_cards
            result = collection.find_one()
            return Card(**result)
        except Exception as exception:
            raise Exception("Error saving data: " + str(exception))

    def get_number_of_items(self, number_of_items) -> List[Card]:
        try:
            collection = self.cards.list_of_cards
            result = collection.find().limit(number_of_items)
            return [Card(**r) for r in result]
        except Exception as exception:
            raise Exception("Error saving data: " + str(exception))

    def get_one_item_from_position(self, position) -> Card:
        try:
            collection = self.cards.list_of_cards
            result = collection.find().skip(position)
            return Card(**result[0])
        except Exception as exception:
            raise Exception("Error saving data: " + str(exception))
