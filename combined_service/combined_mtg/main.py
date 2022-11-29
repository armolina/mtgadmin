from concurrent.futures import ProcessPoolExecutor
import grpc

import uvicorn

from concurrent import futures
from combined_mtg.infrastructure.grpc.connections.grpc_service import GrpcService
from combined_mtg.infrastructure.api.api import app
from combined_mtg.infrastructure.grpc import mtg_card_pb2_grpc

import logging


def main_grpc():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("grpc_process")

    logger.info("Setting up gRPC server")
    grpc_service = GrpcService()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    mtg_card_pb2_grpc.add_CardServiceServicer_to_server(grpc_service, server)

    server.add_insecure_port('[::]:50051')

    logger.info("Starting gRPC server")
    server.start()
    server.wait_for_termination()


def main_rest():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")


def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("main_process")

    with ProcessPoolExecutor() as executor:
        logger.info("Starting two servers in different processes")
        executor.submit(main_grpc)
        executor.submit(main_rest)


if __name__ == "__main__":
    main()
