from fastapi import FastAPI
from api import chain


app = FastAPI()
app.include_router(chain.route)