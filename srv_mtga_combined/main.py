from concurrent.futures import ProcessPoolExecutor
import grpc

import uvicorn
import mtg_card_pb2_grpc

from concurrent import futures
from mtg.connections.grpc_service import GrpcService
from mtg.connections.api_service import app

import logging
import os

def main_grpc():
    grpc_port = os.environ['GRPC_PORT']
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("grpc_process")

    logger.info("Setting up gRPC server")
    grpc_service = GrpcService()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    mtg_card_pb2_grpc.add_CardServiceServicer_to_server(grpc_service, server)

    server.add_insecure_port(f'[::]:{grpc_port}')

    logger.info("Starting gRPC server")
    server.start()
    server.wait_for_termination()


def main_rest():
    api_port = os.environ['API_PORT']
    uvicorn.run(app, host="0.0.0.0", port=api_port, log_level="info")


def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("main_process")

    with ProcessPoolExecutor() as executor:
        logger.info("Starting two servers in different processes")
        executor.submit(main_grpc)
        executor.submit(main_rest)


if __name__ == "__main__":
    main()