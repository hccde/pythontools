import aiohttp
import asyncio
import async_timeout
import json
from pyquery import PyQuery as pq

def get_configure(file_path):
	with open(file_path, 'r') as f:
		data = json.load(f)
		return data

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def request(loop,params):
    async with aiohttp.ClientSession(loop=loop) as session:
        html = await fetch(session, 'http://www.bing.com')
        print(params)
        #when return ,check queue,construct param,
        # print(html)

# async with aiohttp.ClientSession() as session:
#     async with session.get('https://api.github.com/events') as resp:
#         print(resp.status)
#         print(await resp.text())
configure = get_configure('./configure.json')

def main(config):
    maxRequest = configure['maxRequest']
    tasks = []
    for index in range(0,maxRequest):
        print('request url')
        loop = asyncio.get_event_loop()
        tasks.append(loop.create_task(request(loop,index)))
        # loop.run_until_complete(request(loop,index))
    loop.run_until_complete(asyncio.wait(tasks));

main(configure)