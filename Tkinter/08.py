import tkinter

def jdcanvas():
    baseframe = tkinter.Tk()

    cvs = tkinter.Canvas(baseframe,width=300,height=200)
    cvs.pack()
# 一条线需要两个点指明起始前两个X  后两个Y
    cvs.create_line(23,23,190,234)
    cvs.create_text(200,167,text="i love yh")

    baseframe.mainloop()

if __name__ == '__main__':
    jdcanvas()