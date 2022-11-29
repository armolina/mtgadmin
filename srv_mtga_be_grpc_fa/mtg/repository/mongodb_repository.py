import sys
import json
from pymongo import MongoClient

class MongodbRepository():
    def __open_connection(self) -> None:
        client = MongoClient(
            host = '127.0.0.1:27017',
            serverSelectionTimeoutMS = 3000,
            username='root',
            password='pass',
        )
        return client['cards']

    def find_one(self):
        try:
            db = self.__open_connection()
            collection = db.list_of_cards
            result = collection.find_one()
            return result
        except Exception as exception:
            raise Exception('Error saving data: ' + str(exception))

    def get_number_of_items(self, number_of_items):
        try:
            db = self.__open_connection()
            collection = db.list_of_cards
            result = collection.find().limit(number_of_items)
            return result
        except Exception as exception:
            raise Exception('Error saving data: ' + str(exception))
            
    def get_one_item_from_position(self, position):
        try:
            db = self.__open_connection()
            collection = db.list_of_cards
            result = collection.find().skip(position)
            return result[0]
        except Exception as exception:
            raise Exception('Error saving data: ' + str(exception))
