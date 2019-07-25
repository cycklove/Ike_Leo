import tkinter

def mainmenu():

    baseframe = tkinter.Tk()
    baseframe.wm_title("级联菜单")

    menubar = tkinter.Menu(baseframe)

    emenu = tkinter.Menu(menubar)
    for item in ["Copy","Past","Cut"]:
        emenu.add_command(label=item)

    emenu2 = tkinter.Menu(menubar)

    newmenu = tkinter.Menu(emenu2)
    newmenu.add_command(label="one")
    newmenu.add_command(label="two")
    newmenu.add_separator()

    for item2 in ["New","Open","Save"]:
        if item2 == "New":
            emenu2.add_cascade(label=item2, menu=newmenu)
            emenu2.add_separator()
        else:
            emenu2.add_command(label=item2)

    threemenu = tkinter.Menu(newmenu)
    threemenu.add_command(label="3")
    threemenu.add_command(label="33")
    threemenu.add_separator()
    threemenu.add_command(label="333")

    newmenu.add_cascade(label="Three",menu=threemenu)

    menubar.add_cascade(label="File",menu=emenu2)
    menubar.add_cascade(label="Edit",menu=emenu)
    menubar.add_cascade(label="About")

    baseframe["menu"] = menubar

    baseframe.mainloop()

if __name__ == '__main__':
    mainmenu()