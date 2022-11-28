import grpc
import mtg_card_pb2_grpc

from concurrent import futures
from mtg.connections.grpc_service import GrpcService

def main():
    grpc_service = GrpcService()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    mtg_card_pb2_grpc.add_CardServiceServicer_to_server(grpc_service, server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("server started, port: 50051")
    
    server.wait_for_termination()

if __name__ == '__main__':
    main()