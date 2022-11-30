import os
import grpc
import threading

from main import main

from mtg.repository.mongodb_repository import MongodbRepository
from mtg.repository.grpc_repository import GrpcRepository

def test_get_one_card_from_database():
    mongo_user = os.environ['MONGO_USER']
    mongo_pass = os.environ['MONGO_PASS']
    mongo_host = os.environ['MONGO_HOST']

    mongo_repository = MongodbRepository(mongo_user, mongo_pass, mongo_host)
    card = mongo_repository.find_one()

    assert(card["name"]=="Ancestor's Chosen")


def test_expose_one_card_in_gRPC():
    thread_1 = threading.Thread(main())
    thread_1.start()

    print('hola')
