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
		data = eval(f.read())
		return data
def write_file(string):
    fs = open('dest', 'a')
    log = open('configure','w')
    fs.write(string)
    log.write(str(configure))
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
keyinfo = get_configure('keyinfo.json')

def get_proxy():
    proxys = BeautifulSoup(requests.get("http://qsrdk.daili666api.com/ip/?tid="+keyinfo["tid"]+"&num=1","lxml").text).p.contents[0]
    print(proxys)
    return proxys.strip();

proxy = get_proxy();

async def fetch(session, url,params,loop):
    global proxy
    with async_timeout.timeout(300):
        try:
            async with session.post(url,data=str(params),proxy='http://'+proxy,headers = configure['headers']) as response:
                text = await response.text()
        except:
            print(1)
            loop.run_until_complete(loop.shutdown_asyncgens())
            loop.close()
            proxy = get_proxy()
            print('change proxy')
            configure['params']['resultPagination.start']-=configure['params']['resultPagination.limit']
            return '';
        else:
            print(2)
            print(text)
            if len(text)<300:
                proxy = get_proxy()
                print('get proxy')
                loop.run_until_complete(loop.shutdown_asyncgens())
                loop.close()
                configure['params']['resultPagination.start']-=configure['params']['resultPagination.limit']
                return '';
            else:
                return text

async def request(loop,params):
    async with aiohttp.ClientSession(loop=loop) as session:
        html = await fetch(session,configure['url'],params,loop)
        #when return ,check queue,construct param,
        get_info(html)


configure = get_configure('./configure')

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

main();
