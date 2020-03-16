from fastapi import FastAPI
import src.coronauts
import inspect

app = FastAPI()


@app.get("/")
async def read_cases():
    cases = {}
    for [z, coronaut] in inspect.getmembers(src.coronauts, inspect.isclass):
        c = coronaut()
        cases[c.get_country_name()] = await c.get_cases()
    return cases
