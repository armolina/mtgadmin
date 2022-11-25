import grpc
import os

import mtg_card_pb2, mtg_card_pb2_grpc

def main():
    ip = os.environ['MTGA_BE_IP']
    port = os.environ['MTGA_BE_PORT']
     
    with grpc.insecure_channel("srv_mtga_be:50051") as channel:
        stub = mtg_card_pb2_grpc.CardServiceStub(channel)
        request = mtg_card_pb2.EmptyMesssage()
        result = stub.Ping(request)
        print(result)
    print('hola')

if __name__ == '__main__':
    main()