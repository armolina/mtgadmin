import sys
import grpc
from concurrent import futures


class GrpcServer:

    def __init__(self):
        try:
            self.__server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
        except Exception as exception:
            sys.stderr.write("Exception: " + str(exception))
            raise exception

    @property
    def server(self):
        return self.__server