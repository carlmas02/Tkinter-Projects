from tkinter import *
from tkinter import messagebox as tmsg
root = Tk()
root.geometry("600x400")
root.title("Text-Editor")

#function

#file menu
def new_file():
    pass
def open_file():
    pass
def save_file():
    pass
def save_as_file():
    pass
def exit_file():
    a = tmsg.askyesno("Close","Are you sure?")
    if a == True:
        root.destroy()
    else :
        pass

#edit menu
def cut():
    text.event_generate("<<Cut>>")
def copy():
    text.event_generate("<<Copy>>")
def paste():
    text.event_generate("<<Paste>>")

#about
def menu_about():
    a = tmsg.showinfo("WEEKDYCODER","Thanks for using our software, do rate us on the app store !!!")
    return a

#menu
menu_bar = Menu(root)

def menulist():
    #file
    global menu_file
    menu_file = Menu(menu_bar, tearoff = 0)
    menu_bar.add_cascade(label = "File", menu = menu_file)
    root.config(menu = menu_bar)

    #edit
    global menu_edit
    menu_edit = Menu(menu_bar,tearoff = 0)
    menu_bar.add_cascade(label = "Edit",menu =menu_edit )
    root.config(menu = menu_bar)

    # about
    global menu_about
    menu_bar.add_command(label="About", command=menu_about)



def menu_items():
    menu_file.add_command(label="New", accelerator="Ctrl + N", command=new_file)
    menu_file.add_command(label="Open", accelerator="Ctrl + O", command=open_file)
    menu_file.add_command(label="Save", accelerator="Ctrl + S", command=save_file)
    menu_file.add_command(label="Save as", accelerator="Ctrl + Ctrl + S", command=save_as_file)
    menu_file.add_separator()
    menu_file.add_command(label="Exit", accelerator="Alt + F4", command=exit_file)
    #edit
    menu_edit.add_command(label = "Cut", accelerator = "Ctrl + X" ,command = cut)
    menu_edit.add_command(label = "Copy", accelerator = "Ctrl + C", command = copy)
    menu_edit.add_command(label="Paste ", accelerator="Ctrl + V", command= paste)



#frame
short_cut_bar = Frame(root,height = 20,bg = "navajo white").pack(fill ="x")
side_bar = Frame(root,width = 20,padx = 3 ,bg = "light sea green").pack(fill ="y",side = "left")

#scrollbar

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill =Y)

text = Text(root,yscrollcommand = scrollbar.set )
text.pack(fill = BOTH)
scrollbar.config(command = text.yview)



#function callings
menulist()
menu_items()



root.mainloop()
