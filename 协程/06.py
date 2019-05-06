import threading
# 引入异步iO包
import asyncio

#使用协程
#@asyncio.coroutine
async def hello():
    print("hello world! (%s)" % threading.currentThread())
    print("start...... (%s)" % threading.currentThread())
    await asyncio.sleep(5)
    print("done...... (%s)" % threading.currentThread())
    print("hello again! (%s)" % threading.currentThread())

# 启动消息循环
loop = asyncio.get_event_loop()
# 定义任务
tasks = [hello(),hello()]
# asyncio使用wait等待tasks执行
loop.run_until_complete(asyncio.wait(tasks))
# 关系消息循环
loop.close()
