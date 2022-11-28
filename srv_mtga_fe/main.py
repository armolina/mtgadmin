import time
from functools import wraps
from application.grpc.grpc_cards import GrpcCards
from application.api.api_cards import ApiCards

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
def grpc_get_n_cards(number_of_items):
    grpc_cards = GrpcCards('127.0.0.1', '50051')
    result = grpc_cards.get_n_cards(number_of_items)
    return result

@get_execution_time
def api_get_n_cards(number_of_items):
    api_cards = ApiCards()
    result = api_cards.get_n_cards(number_of_items)
    return result

if __name__ == '__main__':
    number_of_items = 100
    api_result = api_get_n_cards(number_of_items)
    grpc_result = grpc_get_n_cards(number_of_items)

    print(len(api_result))
    
    n_items = 0
    for card in grpc_result:
        n_items += 1
    print(n_items)
