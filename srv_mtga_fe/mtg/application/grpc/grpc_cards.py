import grpc
import mtg_card_pb2, mtg_card_pb2_grpc

class GrpcCards():
    def __init__(self, ip, port):
        n_reintentos = 0
        max_reintentos = 3

        self.ip = ip
        self.port = port
        self.channel = grpc.insecure_channel(f'{ip}:{port}')
        self.stub = mtg_card_pb2_grpc.CardServiceStub(self.channel)
                
    
    def get_one_card_from_position(self, iterator, max_items):     
        request = mtg_card_pb2.MongoConstraints(skip=iterator, max_items=max_items)
        result = self.stub.GetNumberMTGCard(request)
        return result

    def get_n_cards(self, number_of_elements):     
        request = mtg_card_pb2.MongoConstraints(max_items=number_of_elements)
        result = self.stub.StreamGetNumberMTGCard(request)
        return result
        
    def close_channel(self):
        self.channel.close()