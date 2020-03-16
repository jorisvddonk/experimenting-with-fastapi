from fastapi import FastAPI
from src.coronauts.FinlandCoronauts import FinlandCoronauts

app = FastAPI()


@app.get("/")
async def read_cases():
    f = FinlandCoronauts()
    cases = {}
    cases[f.get_country_name()] = await f.get_cases()
    return cases
