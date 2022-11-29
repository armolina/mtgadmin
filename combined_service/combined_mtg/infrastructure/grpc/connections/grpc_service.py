import sys

from combined_mtg.infrastructure.grpc import mtg_card_pb2
from combined_mtg.infrastructure.grpc import mtg_card_pb2_grpc
from combined_mtg.infrastructure.repository.mongodb_repository import MongodbRepository


class GrpcService(mtg_card_pb2_grpc.CardServiceServicer):
    def Ping(self, request, context):
        return mtg_card_pb2.PingResponse(result="1")

    def GetMTGCard(self, request, context):
        mongo_repository = MongodbRepository()
        db_result = mongo_repository.find_one()
        result = mtg_card_pb2.MTGCard(name=db_result['name'], mana_cost=db_result['manaCost'])
        return result

    def GetNumberMTGCard(self, request, context):
        mongo_repository = MongodbRepository()
        db_result = mongo_repository.get_one_item_from_position(request.skip)
        return self.make_message(db_result)
    
    def StreamGetNumberMTGCard(self, request, context):
        mongo_repository = MongodbRepository()
        db_result = mongo_repository.get_number_of_items(request.max_items)
        messages = self.generate_messages(db_result)
        return messages


    def generate_messages(self,data_readed):
        messages=[]
        for message in data_readed:
            messages.append(self.make_message(message))
        for msg in messages:
            yield msg
    
    def make_message(self, message):
        return mtg_card_pb2.MTGCard(
            name=message['name'],
            mana_cost=message.get('manaCost'),
            id=message['id']
    )