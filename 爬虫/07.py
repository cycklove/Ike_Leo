import tkinter
from urllib import request,parse
import json

# 点击button调用函数
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
    req = request.Request(url=baseurl, data=data, headers=headers)
    rsp = request.urlopen(req)

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

# entry输入文本后按回车键调用的函数
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
    req = request.Request(url=baseurl, data=data, headers=headers)
    rsp = request.urlopen(req)

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
baseframe.geometry("800x600")
baseframe.wm_title("英汉翻译词典")

photo = tkinter.PhotoImage(file="D:\PycharmProjects\Ike_Leo\爬虫\\bg.gif")#file：t图片路径

lb3 = tkinter.Label(baseframe,text = "",justify = tkinter.LEFT,image = photo,compound = tkinter.CENTER,font=("微软雅黑"))
lb3.place(x=1,y=1,width=800,height=600)

lb1 = tkinter.Label(baseframe,text="请输入需要翻译的内容:",bg="white",fg="green",font=("微软雅黑",18))
#lb1.grid(row=0,column=0,stick=tkinter.W)
lb1.pack()

e1 = tkinter.Entry(baseframe,width=50,insertbackground='green', highlightthickness=1,fg="green")
#e1.grid(row=0,column=1,stick=tkinter.E)
e1.bind("<Return>",reg2)
e1.pack()

btn = tkinter.Button(baseframe,text="确定",command = reg,fg="green",font=("微软雅黑",18),highlightthickness =1)
#btn.grid(row=2,column=1,stick=tkinter.E)
btn.pack()

#lb3 = tkinter.Label(baseframe, text="",image=photo,compound = "center")

lb4 = tkinter.Label(baseframe,text="©Develop:Ike...Leo",bg="white",fg="green",font=("微软雅黑",18))
#lb1.grid(row=0,column=0,stick=tkinter.W)
lb4.place(x=240,y=500)

baseframe.mainloop()