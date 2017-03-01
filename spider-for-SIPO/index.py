import aiohttp
import asyncio
import async_timeout
import json
import copy 
import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

def get_configure(file_path):
	with open(file_path, 'r') as f:
		data = json.load(f)
		return data
def write_file(string):
    fs = open('dest', 'a')
    log = open('configure.json','w')
    fs.write(string)
    log.write(json.dumps(configure))
    log.close();
    fs.close()


def get_file(path):
    fs = open(path,'r')
    return fs.read()
def get_info(str):
    q = pq(str)
    length = len(q('.item-content-body'))
    string = '';
    for index in range(0,length) :
        string+=q('.item-content-body').eq(index).text()+'\n\n'
    write_file(string)
    print(string)

def get_proxy():
    proxys = BeautifulSoup(requests.get("http://qsrdk.daili666api.com/ip/?tid=557761112430648&num=1").text).p.contents[0]
    print proxys
    return proxys.strip();


async def fetch(session, url,params):
    with async_timeout.timeout(20):
        async with session.post(url,data=params) as response:
            text = await response.text()
            if len(text)<300:
                proxy = get_proxy()
                configure['params']['resultPagination.start']-=configure['params']['resultPagination.limit']
            else:
                return text
            return '';

async def request(loop,params):
    async with aiohttp.ClientSession(loop=loop,proxy='http://'+proxy) as session:
        html = await fetch(session,configure['url'],params)
        #when return ,check queue,construct param,
        get_info(html)


configure = get_configure('./configure.json')

def tasks_group(config):
    maxRequest = configure['maxRequest']
    tasks = []
    for index in range(0,maxRequest):
        loop = asyncio.get_event_loop()
        params = copy.deepcopy(configure['params'])
        tasks.append(loop.create_task(request(loop,params)))
        configure['params']['resultPagination.start']+=configure['params']['resultPagination.limit'];        
    loop.run_until_complete(asyncio.wait(tasks));

# tasks_group(configure)
# get_info(get_file('data'))
def main():
    end = configure['params']['resultPagination.totalCount']
    start = configure['params']['resultPagination.start']
    while end >= start:
        tasks_group(configure)
    print('this city ok')

proxy = get_proxy();
main();
