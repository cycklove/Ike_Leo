import tkinter
import re
from colorama import Fore,Back,Style
from urllib import request,parse
import json


def reg():
    baseurl = "https://fanyi.baidu.com/sug"
    # 存放用来模拟from的数据 一定是dict格式
    word = e1.get()

    data = {
        'kw': word
    }
    #print(word)
    # 需要使用parse模块对data进行编码
    data = parse.urlencode(data).encode("utf-8")

    # 需要构造一个请求头 应该至少包含传入的数据的长度
    # request要求传入的请求头是一个dict格式

    headers = {
        # 因为使用post 至少包含content-length 字段
        "Content-Length": len(data)
    }

    rsp = request.urlopen(baseurl, data=data)

    json_data = rsp.read().decode("utf-8")

    json_data = json.loads(json_data)

    test2 = {}

    for item in json_data["data"]:
        test2[item["k"]] = item["v"]

    # ensure_ascii=False来指定出中文
    # indent对json进行数据格式化输出
    aa = json.dumps(test2,ensure_ascii=False, indent=4)

    lb3["fg"] = "red"
    lb3["text"] = aa

def reg2(event):
    baseurl = "https://fanyi.baidu.com/sug"
    # 存放用来模拟from的数据 一定是dict格式
    word = e1.get()

    data = {
        'kw': word
    }
    #print(word)
    # 需要使用parse模块对data进行编码
    data = parse.urlencode(data).encode("utf-8")

    # 需要构造一个请求头 应该至少包含传入的数据的长度
    # request要求传入的请求头是一个dict格式

    headers = {
        # 因为使用post 至少包含content-length 字段
        "Content-Length": len(data)
    }

    rsp = request.urlopen(baseurl, data=data)

    json_data = rsp.read().decode("utf-8")

    json_data = json.loads(json_data)

    test2 = {}

    for item in json_data["data"]:
        test2[item["k"]] = item["v"]

    # ensure_ascii=False来指定出中文
    # indent对json进行数据格式化输出
    aa = json.dumps(test2,ensure_ascii=False, indent=4)

    lb3["fg"] = "red"
    lb3["text"] = aa

baseframe = tkinter.Tk()
baseframe.geometry("600x400")
baseframe.wm_title("英汉翻译词典")

lb1 = tkinter.Label(baseframe,text="请输入需要翻译的内容:")
#lb1.grid(row=0,column=0,stick=tkinter.W)
lb1.pack()

e1 = tkinter.Entry(baseframe,width=50)
#e1.grid(row=0,column=1,stick=tkinter.E)
e1.pack()

btn = tkinter.Button(baseframe,text="确定",command = reg,fg="black")
#btn.grid(row=2,column=1,stick=tkinter.E)
btn.bind("<Return>",reg2)
btn.pack()

lb3 = tkinter.Label(baseframe, text="")
#lb3.grid(row=10, column=1)
lb3.pack()

baseframe.mainloop()