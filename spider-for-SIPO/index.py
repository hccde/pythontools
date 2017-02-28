import aiohttp
import asyncio
import async_timeout
import json
import copy 
from pyquery import PyQuery as pq

def get_configure(file_path):
	with open(file_path, 'r') as f:
		data = json.load(f)
		return data
def write_file(string):
    fs = open('data', 'w')
    fs.write(string)
    fs.close()

async def fetch(session, url,params):
    with async_timeout.timeout(100):
        async with session.post(url,data=params) as response:
            return await response.text()

async def request(loop,params):
    async with aiohttp.ClientSession(loop=loop) as session:
        html = await fetch(session,configure['url'],params)
        #when return ,check queue,construct param,
        write_file(html)
        print(html)

# async with aiohttp.ClientSession() as session:
#     async with session.get('https://api.github.com/events') as resp:
#         print(resp.status)
#         print(await resp.text())
configure = get_configure('./configure.json')

def tasks_group(config):
    maxRequest = configure['maxRequest']
    tasks = []
    for index in range(0,maxRequest):
        print('request url')
        loop = asyncio.get_event_loop()
        params = copy.deepcopy(configure['params'])
        tasks.append(loop.create_task(request(loop,params)))
        configure['params']['resultPagination.start']+=configure['params']['resultPagination.limit'];        
    loop.run_until_complete(asyncio.wait(tasks));
    # configure['current'] +=configure.current+maxRequest;

tasks_group(configure)