from concurrent.futures import ThreadPoolExecutor
import logging
import os

import grpc
from dotenv import load_dotenv
from mtg import mtg_card_pb2_grpc
from mtg.connections.grpc_service import GrpcService

load_dotenv()
SERVICE_PORT: str = os.environ.get("SERVICE_PORT")


def main():
    logger = logging.getLogger("mtga_fe")
    with ThreadPoolExecutor(max_workers=None) as thread_pool:
        server = grpc.server(thread_pool)
        mtg_card_pb2_grpc.add_CardServiceServicer_to_server(GrpcService, server)

        server.add_insecure_port(f"[::]:{SERVICE_PORT}")
        server.start()
        logger.info(f"Server started, port: {SERVICE_PORT}")

        server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
