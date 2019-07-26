import tkinter

baseframe = tkinter.Tk()

def btnclick(event):
    global w
    w.move("ball",12,5)
    w.move("fall",0,5)

w = tkinter.Canvas(baseframe,width=500,height=400)
w.pack()
w.bind("<Button-1>",btnclick)
#创建组件后返回id
id_ball = w.create_oval(20,20,50,50, fill = "yellow",tag="ball")
id_ball2 = w.create_oval(150,150,200,200, fill = "yellow")
w.addtag_withtag("ball",id_ball2)
#创建组件使用tag属性
w.create_text(123,56,fill="red",text="i love yh",tag="fall")
#创建的时候如果没有指定tag可以利用addtag_withtag添加
#同类函数还有addtag_all,addtag_above,addtag_xxx扥等
id_rectangle = w.create_rectangle(56,78,173,110,fill="green")
w.addtag_withtag("fall",id_rectangle)

baseframe.mainloop()
