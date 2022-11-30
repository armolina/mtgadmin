import time
import os
from functools import wraps
from mtg.application.grpc.grpc_cards import GrpcCards
from mtg.application.api.api_cards import ApiCards


def get_execution_time(func):
    @wraps(func)
    def get_execution_time_wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} Took {end_time-start_time:.4f} seconds')
        return result

    return get_execution_time_wrapper


@get_execution_time
def grpc_get_n_unary_cards(number_of_items):
    grpc_server = os.environ['GRPC_SERVER']
    grpc_port = os.environ['GRPC_PORT']

    grpc_cards = GrpcCards(grpc_server, grpc_port)
    
    iterator = 0
    while iterator <= number_of_items:
        result = grpc_cards.get_one_card_from_position(iterator)
        iterator+=1

    return iterator-1

@get_execution_time
def grpc_get_n_stream_cards(number_of_items):
    grpc_server = os.environ['GRPC_SERVER']
    grpc_port = os.environ['GRPC_PORT']

    grpc_cards = GrpcCards(grpc_server, grpc_port)
    result = grpc_cards.get_n_cards(number_of_items)

    return result

@get_execution_time
def api_get_n_cards(number_of_items):
    api_cards = ApiCards()
    result = api_cards.get_n_cards(number_of_items)
    return result

if __name__ == '__main__':
    number_of_items = 1

    api_result = api_get_n_cards(number_of_items)
    grpc_unary_result = grpc_get_n_unary_cards(number_of_items)
    grpc_stream_result = grpc_get_n_stream_cards(number_of_items)

    print('validating responses...')
    n_stream_items = 0
    for card in grpc_stream_result:
        n_stream_items += 1
    
    print(f'{len(api_result)}: api received objects')
    print(f'{grpc_unary_result}: rpc stream received objects')
    print(f'{n_stream_items}: rpc stream received objects')
