import tkinter

def maintk():
    global baseframe
    def makelabel():

        lb1 = tkinter.Label(baseframe,text="我用Python",fg="red")
        lb1.pack()

    baseframe = tkinter.Tk()
    baseframe.wm_title("弹出菜单")
    baseframe.geometry("400x300")

    menubar = tkinter.Menu(baseframe)
    yrcmenu = tkinter.Menu(menubar)
    yrcmenu.add_command(label="3串")
    yrcmenu.add_command(label="5串")
    yrcmenu.add_command(label="10串")

    for x in ["小龙虾","臭豆腐","炸香肠","烧烤"]:
        if x == "烧烤":
            menubar.add_cascade(label=x, menu=yrcmenu)
        else:
            menubar.add_separator()
            menubar.add_command(label=x)


    menubar.add_command(label="牛肉串",command=makelabel)

    def pop(event):
            menubar.post(event.x_root,event.y_root)

    baseframe.bind("<Button-3>",pop)

    baseframe.mainloop()

if __name__ == '__main__':
    maintk()