import os

from mtg.repository.mongodb_repository import MongodbRepository


class GrpcRepository:
    grpc_host = ""
    grpc_port = ""
    grpc_mode = ""

    def __init__(self, grpc_host, grpc_port, grpc_mode):
        self.grpc_host = grpc_host
        self.grpc_port = grpc_port
        self.grpc_mode = grpc_mode

    def get_one_card(self):
        mongo_repository = MongodbRepository(
            os.environ["MONGO_USER"], os.environ["MONGO_PASS"], os.environ["MONGO_HOST"]
        )
        data_readed = mongo_repository.find_one()
        return data_readed
