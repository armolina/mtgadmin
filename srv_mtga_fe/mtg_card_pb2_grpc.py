# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mtg_card_pb2 as mtg__card__pb2


class CardServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/CardService/Ping',
                request_serializer=mtg__card__pb2.EmptyMesssage.SerializeToString,
                response_deserializer=mtg__card__pb2.PingResponse.FromString,
                )
        self.GetCardInfo = channel.unary_unary(
                '/CardService/GetCardInfo',
                request_serializer=mtg__card__pb2.EmptyMesssage.SerializeToString,
                response_deserializer=mtg__card__pb2.CardInfo.FromString,
                )


class CardServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCardInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CardServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=mtg__card__pb2.EmptyMesssage.FromString,
                    response_serializer=mtg__card__pb2.PingResponse.SerializeToString,
            ),
            'GetCardInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCardInfo,
                    request_deserializer=mtg__card__pb2.EmptyMesssage.FromString,
                    response_serializer=mtg__card__pb2.CardInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CardService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CardService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CardService/Ping',
            mtg__card__pb2.EmptyMesssage.SerializeToString,
            mtg__card__pb2.PingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCardInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CardService/GetCardInfo',
            mtg__card__pb2.EmptyMesssage.SerializeToString,
            mtg__card__pb2.CardInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
