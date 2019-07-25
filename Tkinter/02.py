import  tkinter

def baselabel(event):
    '''global baseframe
    lb = tkinter.Label(baseframe,text="谢谢点击")
    lb.pack()'''
    baseframe2 = tkinter.Tk()
    baseframe2.wm_title("ike2")
    btu2 =tkinter.Button(baseframe2,text="哈哈哈！！！",fg="blue")
    btu2.bind("<Button-1>", baselabel2)
    btu2.pack()

    baseframe2.mainloop()

def baselabel2(event):
    baseframe3 = tkinter.Tk()
    baseframe3.wm_title("ike3")
    btu3 = tkinter.Button(baseframe3, text="呵呵呵！！！", fg="GREEN")
    btu3.pack()

    baseframe3.mainloop()





baseframe = tkinter.Tk()
baseframe.wm_title("ike1")

btu = tkinter.Button(baseframe,text="模拟按钮",fg="red")
# 绑定相应的消息和处理函数
# 获取鼠标左键点击 并启动相应的处理函数baselabel
btu.bind("<Button-1>",baselabel)
btu.pack()


baseframe.mainloop()