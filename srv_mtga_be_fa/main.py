from fastapi import FastAPI
from pydantic import BaseModel
from mtg.repository.mongodb_repository import MongodbRepository

app = FastAPI()
class Msg(BaseModel):
    msg: str

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to the API home page!"}

@app.get("/cards")
async def function_demo_get():
    mongo_repository = MongodbRepository()
    result = mongo_repository.get_one_item_from_position(1)
    print(result['name'])
    return {"message": result['name']}

@app.get("/cards/{max_items}")
async def function_demo_get_path_id(max_items: int):
    print(max_items)
    mongo_repository = MongodbRepository()
    result = mongo_repository.get_number_of_items(max_items)
    
    cards=[]
    for item in result:
        cards.append(card_helper(item))
    
    return {"message": cards}

def card_helper(card) -> dict:
    return{
        'name':card['name'],
        'mana_cost':card.get('manaCost'),
        'id':card['id']
    }