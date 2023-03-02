from tkinter import *

def callback():
    print("called the callback!")

root = Tk()

# create a menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open...", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=callback)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)

listbox = Listbox(root)
listbox.pack()
listbox.insert(END, "a list entry")
for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

variable = StringVar(root)
variable.set("one") # default value
w = OptionMenu(root, variable, "one", "two", "three")
w.pack()

mainloop()
