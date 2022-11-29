import time
import logging

from fastapi import Depends, FastAPI, Request

from combined_mtg.application.card import get_a_number_of_cards, get_all_cards
from combined_mtg.infrastructure.repository.mongodb_repository import MongodbRepository
from combined_mtg.infrastructure.repository.repository import CardsRepository


app = FastAPI(
    title=f"MTG Service - 🃏",
    description="",
    version="v1",
)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('fastapi_server')


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"The request took {process_time} seconds")
    response.headers["X-Process-Time"] = str(process_time)
    return response


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
