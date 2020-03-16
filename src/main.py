from fastapi import FastAPI
from src.coronauts.FinlandCoronauts import FinlandCoronauts
from src.coronauts.SwedenCoronauts import SwedenCoronauts

app = FastAPI()


@app.get("/")
async def read_cases():
    f = FinlandCoronauts()
    s = SwedenCoronauts()
    cases = {}
    cases[f.get_country_name()] = await f.get_cases()
    cases[s.get_country_name()] = await s.get_cases()
    return cases
