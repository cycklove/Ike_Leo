import tkinter
import math as m

baseframe = tkinter.Tk()

w= tkinter.Canvas(baseframe,width=300,height=300,bg="red")
w.pack()

center_x = 150
center_y = 150

r = 150

point = [
    #左上点
    center_x - int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    #右上点
    center_x + int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    #左下点
    center_x - int(r * m.sin( m.pi / 5)),
    center_y + int(r * m.cos( m.pi / 5)),
    #顶点
    center_x,
    center_y - r,
    #右下点
    center_x + int(r * m.sin(m.pi / 5)),
    center_y + int(r * m.cos(m.pi / 5)),
]

w.create_polygon(point,outline="red",fill="yellow")
w.create_text(150,150,text="五角星",fill="red")

baseframe.mainloop()