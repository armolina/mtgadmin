import sys
from threading import Thread
import mtg_card_pb2, mtg_card_pb2_grpc

class GrpcService(mtg_card_pb2_grpc.CardServiceServicer):
    def Ping(self, request):
        return mtg_card_pb2.PingResponse(result="1")