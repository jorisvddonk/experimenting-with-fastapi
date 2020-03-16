from . import coronauts
import aiohttp
import asyncio
from src.parsers.RIVMParser import parse

class NetherlandsCoronauts(coronauts.Coronauts):
   
    async def get_cases(self):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://www.rivm.nl/nieuws/actuele-informatie-over-coronavirus') as response:
                text = await response.text()
                return parse(text)

    def get_country_name(self):
        return 'The Netherlands'
