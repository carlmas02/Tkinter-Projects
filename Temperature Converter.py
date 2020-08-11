from tkinter import *

root = Tk()
root.title("Temperature Converter")
root.geometry("440x120")
#root.minsize(width= 400, height=100)
#root.maxsize(width= 400, height=100)
root.config(bg = "cyan")

temp = StringVar()

def get_temp():
    result = Temp_entry.get()
    mas = round((int(result)-32)*(5/9))
    frame.config(text=  str(mas) + "°C" )
    #frame.delete(0, END)




Temp_entry = Entry(root,textvariable = temp)
Temp_entry.pack(side = LEFT,padx = 10)

label = Label(root,text = "°F", bg  = "cyan")
label.pack(side= LEFT)


button = Button(root,text = "➡",font = "comicsans",height = 2,width = 5,bg = "navajo white",command = get_temp)
button.pack(side = LEFT,padx = 40)

frame = Label(root,bg = "cyan",text = "",font = "verdana")
frame.pack(side = LEFT,padx = 50)



root.mainloop()