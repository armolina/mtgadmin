import logging
from typing import List

from mtg.domain.card import Card
from mtg.repository.card_repository import CardsRepository

logger = logging.getLogger("fastapi_server")

def get_all_cards(repository: CardsRepository) -> str:
    result = repository.get_one_item_from_position(1)
    card_name = result.name
    logger.info(card_name)
    return card_name

def get_a_number_of_cards(max_items: int, repository: CardsRepository) -> List[Card]:
    logger.info(max_items)
    return repository.get_number_of_items(max_items)