from . import coronauts
import aiohttp
import asyncio

class FinlandCoronauts(coronauts.Coronauts):
   
    async def get_cases(self):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/finnishCoronaData') as response:
                json = await response.json()
                print(json)
                return len(json['confirmed'])

    def get_country_name(self):
        return 'Finland'
