from fastapi import FastAPI
import src.coronauts
import inspect
import asyncio

app = FastAPI()


@app.get("/")
async def read_cases():
    cases = {}
    coronautObjects = [coronaut() for [z, coronaut] in inspect.getmembers(src.coronauts, inspect.isclass)]
    done, pending = await asyncio.wait([c.get_cases() for c in coronautObjects], timeout=3)
    for i, task in enumerate(done):
        amount = task.result()
        cases[coronautObjects[i].get_country_name()] = amount
    return cases
