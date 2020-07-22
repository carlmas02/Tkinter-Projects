from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

root.title("FORMULA SHEET")
root.geometry("2000x400")
root.configure(bg = "aquamarine")
root.minsize(height = 400, width = 407)


#function


def close_info():
    a = tmsg.askyesno("Close","Are you sure ?")
    if a == True:
        return root.destroy()
    else :
        pass

def abouter():
    print(tmsg.showinfo("Carls software", "Hello , I am an amaetur devlepor inspiring to become a pro. developer"))

def sinx_soln():
    a = sin_x.set("cosx")
    print(a)

def cosx_soln():
    return cos_x.set("-sinx")

def tanx_soln():
    return tan_x.set("sec^2x")
def secx_soln():
    return sec_x.set("secx.tanx")
def cotx_soln():
    return cot_x.set("-cosec^2x")
def cscx_soln():
    return csc_x.set("-cscx.cotx")



#menu

close = Menu(root)
close.add_command(label = "Close" ,command = close_info )
root.config(menu = close )
close.add_command(label = "About" ,command = abouter )


#frame
frame_1 = Frame(root, bg = "red", borderwidth = 8 ,relief = SUNKEN)
frame_2 = Frame(root, bg = "black", borderwidth = 8 ,relief = SUNKEN )


#label
label = Label(root,width = 10 , bg = "aquamarine").grid(column = 1)
label = Label(root,width = 10 , bg = "aquamarine").grid(column = 3)
label = Label(root,width = 10 , bg = "aquamarine").grid(column = 5)
label = Label(root,width = 10 , bg = "aquamarine").grid(column = 7)
label = Label(root,width = 10 , bg = "aquamarine").grid(column = 9)


#variable
sin_x = StringVar()
cos_x = StringVar()
tan_x = StringVar()
sec_x = StringVar()
cot_x = StringVar()
csc_x = StringVar()


#entry
sinx_solution = Entry(root, relief = GROOVE, bg = "light grey" ,textvariable = sin_x ,font = "fixedsys" )
cosx_solution = Entry(root, relief = GROOVE, bg = "light grey" ,textvariable = cos_x ,font = "fixedsys" )
tanx_solution = Entry(root, relief = GROOVE, bg = "light grey", textvariable = tan_x, font = "fixedsys" )
secx_solution = Entry(root, relief = GROOVE, bg = "light grey", textvariable = sec_x, font = "fixedsys" )
cotx_solution = Entry(root, relief = GROOVE, bg = "light grey", textvariable = cot_x, font = "fixedsys" )
cscx_solution = Entry(root, relief = GROOVE, bg = "light grey", textvariable = csc_x, font = "fixedsys" )


#label
diff = Label(frame_1, text ="d/dx" ,padx = 60 )


#button
sinx = Button(root,text = "SIN(X)", pady = 10 ,padx = 10 ,command = sinx_soln )
cosx = Button(root,text = "COS(X)" , pady = 10 ,padx = 10,command = cosx_soln )
tanx = Button(root,text = "TAN(X)" , pady = 10 ,padx = 10,command = tanx_soln )
secx = Button(root,text = "SEC(X)" , pady = 10 ,padx = 10,command = secx_soln )
cotx = Button(root,text = "COT(X)" , pady = 10 ,padx = 10,command = cotx_soln )
cscx = Button(root,text = "CSC(X)" , pady = 10 ,padx = 10,command = cscx_soln )




#grid()
diff.grid()
frame_1.grid(column = 0, row =1)
frame_2.grid(column = 0,row = 5)
sinx.grid(row = 2 , column = 0)
cosx.grid(row = 2, column = 2)
tanx.grid(row =2, column = 4)
secx.grid(row=2 ,column = 6)
cotx.grid(row=2 ,column = 8)
cscx.grid(row =2,column = 10)
sinx_solution.grid(row =3 )
cosx_solution.grid(row = 3,column = 2)
tanx_solution.grid(row = 3, column = 4)
secx_solution.grid(row= 3, column = 6)
cotx_solution.grid(row = 3,column = 8)
cscx_solution.grid(row=3, column = 10)



#for integration

#function
def Sinx_soln():
    b = Sin_x.set("-cosx + c")
    print(b)

def Cosx_soln():
    return Cos_x.set("sinx + c")

def Tanx_soln():
    return Tan_x.set("log|secx| + c")
def Secx_soln():
    return Sec_x.set("tanx + c")
def Cotx_soln():
    return Cot_x.set("log|sinx| + c")
def Cscx_soln():
    return Csc_x.set("-log|cscx+tanx| + c")



#frame

#label
integ = Label(frame_2 , text ="XdX", padx = 60 )
integ.grid(row = 4)

#variable
Sin_x = StringVar()
Cos_x = StringVar()
Tan_x = StringVar()
Sec_x = StringVar()
Cot_x = StringVar()
Csc_x = StringVar()

#entry
Sinx_solution = Entry(root, relief = GROOVE, bg = "light grey" ,textvariable = Sin_x ,font = "fixedsys" ).grid(row =7,column = 0)
Cosx_solution = Entry(root, relief = GROOVE, bg = "light grey" ,textvariable = Cos_x ,font = "fixedsys" ).grid(row = 7 ,column = 2)
Tanx_solution = Entry(root, relief = GROOVE, bg = "light grey", textvariable = Tan_x, font = "fixedsys" ).grid(row = 7 ,column = 4)
Secx_solution = Entry(root, relief = GROOVE, bg = "light grey", textvariable = Sec_x, font = "fixedsys" ).grid(row = 7 ,column = 6)
Cotx_solution = Entry(root, relief = GROOVE, bg = "light grey", textvariable = Cot_x, font = "fixedsys" ).grid(row = 7 ,column = 8)
Cscx_solution = Entry(root, relief = GROOVE, bg = "light grey", textvariable = Csc_x, font = "fixedsys" ).grid(row = 7 ,column = 10)




#button
Sinx = Button(root,text = "SIN(X)", pady = 10 ,padx = 10 ,command = Sinx_soln ).grid(row = 6)
Cosx = Button(root,text = "COS(X)" , pady = 10 ,padx = 10,command = Cosx_soln ).grid(row = 6 ,column = 2)
Tanx = Button(root,text = "TAN(X)" , pady = 10 ,padx = 10,command = Tanx_soln ).grid(row = 6 ,column = 4)
Secx = Button(root,text = "SEC(X)" , pady = 10 ,padx = 10,command = Secx_soln ).grid(row = 6 ,column = 6)
Cotx = Button(root,text = "COT(X)" , pady = 10 ,padx = 10,command = Cotx_soln ).grid(row = 6 ,column = 8)
Cscx = Button(root,text = "CSC(X)" , pady = 10 ,padx = 10,command = Cscx_soln ).grid(row = 6 ,column = 10)



root.mainloop()