from tkinter import *

root = Tk()

root.title("Simple Calculator")
root.minsize(height = 320,width = 231)


e = Entry(root, width = 35 , borderwidth = 5)

e.grid(row = 0, column = 0,padx = 5, pady =5,columnspan = 3)

#function
def button_ad(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_delete():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_nums
    f_nums = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    e.insert(0,f_nums + int(second_number))

#button
button_1 = Button(root, text = "1" ,padx = 20, pady =10,command = lambda: button_ad(1) )
button_2 = Button(root, text = "2" ,padx = 20, pady =10,command = lambda: button_ad(2) )
button_3 = Button(root, text = "3" ,padx = 20, pady =10,command = lambda: button_ad(3) )
button_4 = Button(root, text = "4" ,padx = 20, pady =10,command = lambda: button_ad(4) )
button_5 = Button(root, text = "5" ,padx = 20, pady =10,command = lambda: button_ad(5) )
button_6 = Button(root, text = "6" ,padx = 20, pady =10,command = lambda: button_ad(6) )
button_7 = Button(root, text = "7" ,padx = 20, pady =10,command = lambda: button_ad(7) )
button_8 = Button(root, text = "8" ,padx = 20, pady =10,command = lambda: button_ad(8) )
button_9 = Button(root, text = "9" ,padx = 20, pady =10,command = lambda: button_ad(9) )
button_0 = Button(root, text = "0" ,padx =20, pady =10,command = lambda: button_ad(0) )
button_add = Button(root, text = "+" ,padx = 20, pady =10,command = button_add )
button_subtract = Button(root, text = "-" ,padx = 20, pady =10,command = button_add )
button_multiply = Button(root, text = "x" ,padx = 20, pady =10,command = button_add )
button_divide = Button(root, text = "/" ,padx = 20, pady =10,command = button_add )
button_equal = Button(root, text = "=" , padx = 20, pady =10,command = button_equal )
button_clear = Button(root, text = "CLEAR" , padx = 30, pady =10, command = button_delete )

#button on screen
button_1.grid(row =3 , column = 0)
button_2.grid(row =3 , column = 1)
button_3.grid(row =3 , column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row =1 , column = 0)
button_8.grid(row =1 , column = 1)
button_9.grid(row =1 , column = 2)

button_0.grid(row = 4 ,column = 0)

button_add.grid(row = 5, column = 1,columnspan = 2)
button_clear.grid(row = 4, column = 1, columnspan = 2)
button_equal.grid(row = 5, column = 0)
button_subtract.grid(row = 6, column = 0)
button_multiply.grid(row = 6, column = 1)
button_divide.grid(row = 6, column = 2)

root.mainloop()