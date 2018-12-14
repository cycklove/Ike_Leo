# 异常
- 广义上的错误分为错误和异常
- 错误指的是可以人为避免
- 异常是指在语法逻辑正确的前提下 出现的问题
- 在Python里 异常是一个类 可以处理和使用
# 异常的分类
 - BaseException	所有异常的基类
 - SystemExit	解释器请求退出
 - KeyboardInterrupt	用户中断执行(通常是输入^C)
 - Exception	常规错误的基类
 - StopIteration	迭代器没有更多的值
 - GeneratorExit	生成器(generator)发生异常来通知退出
 - SystemExit	Python 解释器请求退出
 - StandardError	所有的内建标准异常的基类
 - ArithmeticError	所有数值计算错误的基类
 - FloatingPointError	浮点计算错误
 - OverflowError	数值运算超出最大限制
 - ZeroDivisionError	除(或取模)零 (所有数据类型)
 - AssertionError	断言语句失败
 - AttributeError	对象没有这个属性
 - EOFError	没有内建输入,到达EOF 标记
 - EnvironmentError	操作系统错误的基类
 - IOError	输入/输出操作失败
 - OSError	操作系统错误
 - WindowsError	系统调用失败
 - ImportError	导入模块/对象失败
 - KeyboardInterrupt	用户中断执行(通常是输入^C)
 - LookupError	无效数据查询的基类
 - IndexError	序列中没有没有此索引(index)
 - KeyError	映射中没有这个键
 - MemoryError	内存溢出错误(对于Python 解释器不是致命的)
 - NameError	未声明/初始化对象 (没有属性)
 - UnboundLocalError	访问未初始化的本地变量
 - ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
 - RuntimeError	一般的运行时错误
 - NotImplementedError	尚未实现的方法
 - SyntaxError	Python 语法错误
 - IndentationError	缩进错误
 - TabError	Tab 和空格混用
 - SystemError	一般的解释器系统错误
 - TypeError	对类型无效的操作
 - ValueError	传入无效的参数
 - UnicodeError	Unicode 相关的错误
 - UnicodeDecodeError	Unicode 解码时的错误
 - UnicodeEncodeError	Unicode 编码时错误
 - UnicodeTranslateError	Unicode 转换时错误
 - Warning	警告的基类
 - DeprecationWarning	关于被弃用的特征的警告
 - FutureWarning	关于构造将来语义会有改变的警告
 - OverflowWarning	旧的关于自动提升为长整型(long)的警告
 - PendingDeprecationWarning	关于特性将会被废弃的警告
 - RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
 - SyntaxWarning	可疑的语法的警告
 - UserWarning	用户代码生成的警告
 
 # 异常处理
 - 不能保证程序永远正确运行
 - 但是 必须保证程序在最坏的情况下得到的问题被妥善处理
 - Python的异常处理模块全部语法为
 
        try:
            尝试实现某个操作
            如果没有异常 任务就可以完成
            如果出现异常 将异常从当前代码块扔出去尝试解决异常
        except 异常类型1：
            解决方案1：用于尝试在此处处理异常解决问题
            
        except 异常类型2：
            解决方案2：用于尝试在此处处理异常解决问题
        
        except (异常类型1，异常类型2...)
            解决方案: 针对多个异常使用相同的处理方式
            
        except：
            解决方案：所有异常的解决方案
            
        else：
            如果没有出现任何异常 将会执行此处代码
            
        finally：
            管你有没有异常都要执行的代码
            
- 流程
    1.执行try下面的语句
    2.如果出现异常 则在except语句里查找对应异常并进行处理
    3.如果没有出现异常 则执行else语句内容
    4.最后不管是否出现异常 都要执行finally语句
- 除except（最少一个）以外 else和finally可选 

# 用户手动引发异常
- 当某些情况 用户希望自己引发一个异常的时候 可以使用
- raise 关键字来引发异常

# 关于自定义异常
- 只要是raise异常 则推荐自定义异常
- 在自定义异常的时候 一般包含以下内容
    - 自定义发生异常的异常代码
    - 自定义发生异常后的问题提示
    - 自定义发生异常的行数
- 最终目的是 一旦发生异常 方便快速定位错误现场         

           