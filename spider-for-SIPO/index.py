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
        # data = json.load(f)
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
def get_info(html_str):
    try:
        q = pq(html_str)
        length = len(q('.item-content-body'))
        string = '';
        for index in range(0,length) :
            string+=q('.item-content-body').eq(index).text()+'\n\n'
    except:
        print(html_str)
        print('parse html error');
        string = ''
    write_file(string)
    print(string)

keyinfo = get_configure('keyinfo.json')

def get_proxy():
    proxys = BeautifulSoup(requests.get("http://qsrdk.daili666api.com/ip/?tid="+keyinfo["tid"]+"&num=1","lxml").text).p.contents[0]
    print(proxys)
    return proxys.strip();

proxy = get_proxy()
dirty = False
def changeProxy():
    if dirty:
        return
    global proxy
    proxy = get_proxy()
    configure['params']['resultPagination.start']-=configure['params']['resultPagination.limit']
    print('change proxy')

async def fetch(session, url,params,loop):
    global proxy
    global dirty
    with async_timeout.timeout(50):
        try:
            async with session.post(url,data=params,proxy='http://'+proxy) as response:
                text = await response.text()
        except:
            print(1)
            dirty = True
            changeProxy()
            # configure['params']['resultPagination.start']-=configure['params']['resultPagination.limit']
            return '';
        else:
            print(2)
            print(text)
            if len(text)<1000:
                dirty = True
                changeProxy()
                return '';
            else:
                return text

async def request(loop,params):
    async with aiohttp.ClientSession(loop=loop) as session:
        html = await fetch(session,configure['url'],params,loop)
        #when return ,check queue,construct param,
        get_info(html)


configure = get_configure('configure')

# def tasks_group(config):
#     maxRequest = configure['maxRequest']
#     tasks = []
#     for index in range(0,maxRequest):
#         loop = asyncio.get_event_loop()
#         params = copy.deepcopy(configure['params'])
#         tasks.append(loop.create_task(request(loop,params)))
#         configure['params']['resultPagination.start']+=configure['params']['resultPagination.limit'];        
#     loop.run_until_complete(asyncio.wait(tasks));

# tasks_group(configure)
# get_info(get_file('data'))
async def main(loop):
    global dirty
    end = configure['params']['resultPagination.totalCount']
    start = configure['params']['resultPagination.start']
    while end >= start:
        maxRequest = configure['maxRequest']
        tasks = []
        dirty = False
        loop = asyncio.get_event_loop()
        for index in range(0,maxRequest):
            params = copy.deepcopy(configure['params'])
            tasks.append(loop.create_task(request(loop,params)))
            configure['params']['resultPagination.start']+=configure['params']['resultPagination.limit'];        
        # loop.run_until_complete(asyncio.wait(tasks));
        await asyncio.wait(tasks)
    # tasks_group(configure)
    # print('this city ok')
loop = asyncio.get_event_loop()
maintask = asyncio.ensure_future(main(loop))
loop.run_until_complete(maintask);
