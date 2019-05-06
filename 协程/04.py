from collections import namedtuple

ResClass = namedtuple("Res","count average")

# 子生成器
def averager():
    total = 0.0
    count = 0
    averager = None

    while True:
        term = yield
        # None是哨兵值
        if term is None:
            break
        total += term
        count += 1
        averager = round(total / count,4)

    return ResClass(count,averager)

# 委派生成器
def grouper(storages,key):
    while True:
        # 获取average()返回的值
        storages[key] = yield from averager()

# 客户端代码
def client():
    process_data = {
    "boys_2":[39.0,40.8,43.2,40.8,43.1,38.6,41.4,40.6,36.3],
    "boys_1":[1.38,1.5,1.32,1.25,1.37,1.48,1.25,1.49,1.46]
    }

    storages = {}
    for k,v in process_data.items():
        # 获得协程
        coroutine = grouper(storages,k)

        # 预激协程
        next(coroutine)

        #发送数据到协程
        for dt in v:
            coroutine.send(dt)

        # 终止协程
        coroutine.send(None)
    print(storages)

# run
client()