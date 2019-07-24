import tkinter

# hello world

base = tkinter.Tk()
# 负责标题
base.wm_title("Label Ike")

lb = tkinter.Label(base,text="Python Label",background="green",fg="red")
btn = tkinter.Button(base,text="an niu")
btn.pack(side=tkinter.LEFT,expand=tkinter.YES,fill=tkinter.Y)
#给相应组件制定布局
lb.pack()
btn.pack()
# 消息循环
base.mainloop()

base2 = tkinter.Tk()
base2.wm_title("Label Ike2")

lb1 = tkinter.Label(base2,text="账号")
lb1.grid(row=0,sticky=tkinter.W)

en1 = tkinter.Entry(base2)
en1.grid(row=0,column=1,sticky=tkinter.E)

lb2 = tkinter.Label(base2,text="密码")
lb2.grid(row=1,sticky=tkinter.W)

en2 = tkinter.Entry(base2)
en2.grid(row=1,column=1,sticky=tkinter.E)

btn2=tkinter.Button(base2,text="登录")
btn2.grid(row=2,column=1,sticky=tkinter.S)

base2.mainloop()