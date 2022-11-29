from fastapi import Depends, FastAPI

from mtg.application.card import get_a_number_of_cards, get_all_cards
from mtg.infrastructure.repository.mongodb_repository import MongodbRepository
from mtg.infrastructure.repository.repository import CardsRepository

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to the API home page!"}


@app.get("/cards")
def function_demo_get(repository: CardsRepository = Depends(MongodbRepository)):
    result = get_all_cards(repository)
    return {"message": result}


@app.get("/cards/{max_items}")
def function_demo_get_path_id(
    max_items: int, repository: CardsRepository = Depends(MongodbRepository)
):
    result = get_a_number_of_cards(max_items, repository)
    return {"message": result}
