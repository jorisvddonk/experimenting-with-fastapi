from fastapi import FastAPI
import src.coronauts
import inspect
import asyncio

app = FastAPI()

async def getData(coronaut):
    return {
        'country': coronaut.get_country_name(),
        'cases': await coronaut.get_cases()
    }

@app.get("/")
async def read_cases():
    cases = {}
    coronautObjects = [coronaut() for [z, coronaut] in inspect.getmembers(src.coronauts, inspect.isclass)]
    done, pending = await asyncio.wait([getData(c) for c in coronautObjects], timeout=3)
    for task in done:
        result = task.result()
        cases[result['country']] = result['cases']
    return cases
