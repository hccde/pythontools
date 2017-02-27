import aiohttp
import asyncio
import async_timeout
import json
from pyquery import PyQuery as pq

def get_configure(file_path):
	with open(file_path, 'r') as f:
		data = json.load(f)
		print(data)

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        html = await fetch(session, 'http://python.org')
        print(html)

# async with aiohttp.ClientSession() as session:
#     async with session.get('https://api.github.com/events') as resp:
#         print(resp.status)
#         print(await resp.text())
get_configure('./configure.json');
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))