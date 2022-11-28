import logging
import os

import grpc
from dotenv import load_dotenv

from mtg import mtg_card_pb2, mtg_card_pb2_grpc

load_dotenv()
GRPC_PRODUCER_HOST: str = os.environ.get("GRPC_PRODUCER_HOST", "localhost")
GRPC_PRODUCER_PORT: str = os.environ.get("GRPC_PRODUCER_PORT")


def main():
    logger = logging.getLogger("mtga_fe")
    with grpc.insecure_channel(f"{GRPC_PRODUCER_HOST}:{GRPC_PRODUCER_PORT}") as channel:
        stub = mtg_card_pb2_grpc.CardServiceStub(channel)
        request = mtg_card_pb2.EmptyMesssage()
        result = stub.Ping(request)
        logger.info(result)
    logger.info("Hi there!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
