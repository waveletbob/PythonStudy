### 异步IO ###

CPU速度与IO设备不匹配，多线程/多进程、异步IO（当线程没办法再多加时）是解决方案。

消息模型，线程只发出IO请求，不等待IO结果，直接进入下一次消息循环继续进行消息处理。

### 协程 ###

Coroutime，子程序（函数）调用时在栈中顺序执行，而协程在执行子程序时可以中断，也就是执行顺序可以变化，


- 不是在多线程种切换而是在一个线程中进行，因此，具有极高的执行效率。
- 不需要多线程的锁机制，只需要判断状态，因此效率比多线程高
- 实现：generator，

``` python

	def consumer():
	    r = ''
	    while True:
	        n = yield r
	        if not n:
	            return
	        print('[CONSUMER] Consuming %s...' % n)
	        r = '200 OK'

	def produce(c):
	    c.send(None)
	    n = 0
	    while n < 5:
	        n = n + 1
	        print('[PRODUCER] Producing %s...' % n)
	        r = c.send(n)
	        print('[PRODUCER] Consumer return: %s' % r)
	    c.close()
	
	c = consumer()
	produce(c)

```
### asyncio ###

消息循环的编程模型

```python

import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):并不会等待，而是直接执行下一个消息循环
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()

```
```python

import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

```

### aiohttp ###

pip install aiohttp

用于实现基于asyncio的HTTP框架





