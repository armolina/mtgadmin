import requests
import os

class ApiCards():
    def __init__(self):
        self.api_server = os.environ['API_SERVER']
        self.api_port = os.environ['API_PORT']

    def get_one_card_from_position(self, from_position):
        response = requests.get(f'{self.api_server}:{self.api_port}/cards')
        return(response.json()['message'])

    def get_n_cards(self, number_of_elements):
        response = requests.get(f'{self.api_server}:{self.api_port}/cards/{number_of_elements}')
        return(response.json()['message'])