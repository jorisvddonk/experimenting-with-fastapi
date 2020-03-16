from . import coronauts
import aiohttp
import asyncio
from src.parsers.FolkhalsomyndighetenParser import parse

class SwedenCoronauts(coronauts.Coronauts):
   
    async def get_cases(self):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/aktuellt-epidemiologiskt-lage/') as response:
                text = await response.text()
                return parse(text)

    def get_country_name(self):
        return 'Sweden'
