#coding:utf-8
import threading
import asyncio

# @asyncio.coroutine
# def print1():
# 	print('hello (%s)' %threading.currentThread())
# 	yield from asyncio.sleep(1)
# 	print('hello (%s)'%threading.currentThread())
# loop=asyncio.get_event_loop()
# tasks=[print1(),print1()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

#实现同一线程并发获取连接sina、sohu、hao123等网页内容
# @asyncio.coroutine
# def spider(host):
# 	print('get from %s...'%host)
# 	connect=asyncio.open_connection(host,80)
# 	reader,writer=yield from connect
# 	header='GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
# 	writer.write(header.encode('utf-8'))
# 	yield from writer.drain()
# 	while True:
# 		line=yield from reader.readline()
# 		if line==b'\r\n':
# 			break
# 		print('%s header > %s'%(host,line.decode('utf-8').rstrip()))
# 	writer.close()
# loop=asyncio.get_event_loop()
# tasks=[spider(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

'''
新代码
1、把@asyncio.coroutine替换为async；
2、把yield from替换为await。
'''

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


