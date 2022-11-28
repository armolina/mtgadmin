from mtg import mtg_card_pb2
from mtg import mtg_card_pb2_grpc


class GrpcService(mtg_card_pb2_grpc.CardServiceServicer):

    def Ping(self, _):
        return mtg_card_pb2.PingResponse(result="1")
