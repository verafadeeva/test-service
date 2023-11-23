import aiohttp
import asyncio
import json
import sys

from db.query import get_information, insert_data


URL_AGE = "https://api.agify.io"
URL_GENDER = "https://api.genderize.io"
URL_NATIONALITY = "https://api.nationalize.io"


async def get_data(name: str) -> dict:
    async with aiohttp.ClientSession() as session:
        params = {'name': name}
        data = {}
        data['name'] = name
        async with session.get(URL_AGE, params=params) as resp:
            result = await resp.json()
            data['age'] = result.get('age')
        async with session.get(URL_GENDER, params=params) as resp:
            result = await resp.json()
            data['gender'] = result.get('gender')
        async with session.get(URL_NATIONALITY, params=params) as resp:
            result = await resp.json()
            data['nationality'] = result.get('country')[0].get('country_id')
        return data


async def main():
    _argv = sys.argv
    if len(_argv) != 2:
        sys.exit("Usage: python main.py NAME")

    name = _argv[1]
    result = get_information(name)

    if not result:
        data = await get_data(name)
        insert_data(data)

    else:
        data = {
            'name': result[0][1],
            'age': result[0][3],
            'gender': result[0][2],
            'nationality': result[0][4],
            'created_at': result[0][5],
        }
    print(json.dumps(data, indent=4))

if __name__ == '__main__':
    asyncio.run(main())
