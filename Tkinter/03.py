import tkinter
import re
from colorama import Fore,Back,Style

def reg():
    # 从输入框中得到用户的输入
    name = e1.get()
    pwd = e2.get()

    t1 = len(name)
    t2 = len(pwd)

    p = re.compile(r'[^A-Za-z0-9]')

    #if name =="111" and pwd == "222":
    if p.match(name) and p.match(pwd):
        lb3["fg"] = "red"
        lb3["text"] = "用户名或密码错误"
        e1.delete(0, t1)
        e2.delete(0, t2)
    else:
        lb3["fg"] = "green"
        lb3["text"] = "登录成功"

baseframe = tkinter.Tk()

lb1 = tkinter.Label(baseframe,text="用户名:")
lb1.grid(row=0,column=0,stick=tkinter.W)

e1 = tkinter.Entry(baseframe)
e1.grid(row=0,column=1,stick=tkinter.E)

lb2 = tkinter.Label(baseframe,text="密码:")
lb2.grid(row=1,column=0,stick=tkinter.W)

e2 = tkinter.Entry(baseframe)
e2.grid(row=1,column=1,stick=tkinter.E)
e2["show"]="*"

btn = tkinter.Button(baseframe,text="登录",command = reg,fg="black")
btn.grid(row=2,column=1,stick=tkinter.E)

lb3 = tkinter.Label(baseframe, text="")
lb3.grid(row=3, column=1)

baseframe.mainloop()