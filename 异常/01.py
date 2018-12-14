'''num = int(input("请输入数字："))
if num != 0:
    print(100/num)
else:
    print("输入的数字不能为0")'''

# 简单异常案例
# 给出提示信息
import traceback
try:
    num = int(input("请输入数字："))
    rst = 100/num
    print("计算结果是：{0}".format(rst))
# 捕获异常后 把异常实例化 出错信息会在实例里
# 以下语句是捕获ZeroDivisionError异常并实例化实例e
except Exception as e:
    print("你输的啥玩意")
    print(repr(e)) # 给出较全的异常信息，包括异常信息的类型，如1/0的异常信息
    traceback.print_exc() # 需要导入traceback模块，此时获取的信息最全
    exit()

# raise案例
# 自定义异常
# 需要注意 自定义异常必须是系统异常的子类
class LeoValueError(ValueError):
    pass
try:
    print("我爱我爱我爱")
    print(18181818181)
    # 手动引发一个异常
    raise LeoValueError
    print("还没完啊")
except Exception as e:
    print("异常啊")
    print(repr(e))
    traceback.print_exc()
finally:
    print("我肯定得执行")

# else语句案例
try:
    num = int(input("请输入数字："))
    rst = 100 / num
    print("计算结果是：{0}".format(rst))
except Exception as e:
    print(repr(e))
else:
    print("没异常")
finally:
    print("反正我会来")