import requests

class ApiCards():
    def get_one_card_from_position(self, from_position):
        response = requests.get('http://localhost:8000/cards')
        return(response.json()['message'])

    def get_n_cards(self, number_of_elements):
        response = requests.get(f'http://localhost:8000/cards/{number_of_elements}')
        return(response.json()['message'])