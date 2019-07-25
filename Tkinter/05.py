import tkinter

baseframe = tkinter.Tk()
baseframe.wm_title("菜单")

menubar = tkinter.Menu(baseframe)
for item in ["File","Edit","View","About"]:
    menubar.add_command(label=item)

baseframe["menu"] = menubar
baseframe.mainloop()