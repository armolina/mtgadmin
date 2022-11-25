import sys
import json
from pymongo import MongoClient

class MongodbRepository():
    __user = ''
    __pwd = ''
    __host = ''
    connection = None

    def __init__(self, user, pwd, host):
        self.__user = user
        self.__pwd = pwd
        self.__host = host

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
