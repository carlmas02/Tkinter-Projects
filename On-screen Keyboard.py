#backspace,enter not working 

from tkinter import *
import pyautogui

root = Tk()

root.geometry("1020x355")
root.title("Carl's Keyboard")
root.config(bg = 'grey11')
#root.wm_attributes("-alpha",0.8)



#function
exp = " "

def button(symbol):
   global exp
   exp += str(symbol)
   exp = exp.lower()
   exp = exp.capitalize()   
   vars.set(exp)
      
      
def clear():
   global exp
   exp = " "
   vars.set(exp)
   
def backspace():
   return pyautogui.press('backspace')

#variable
vars = StringVar()

   
#entry
field = Entry(root,width = 120,textvariable = vars)
field.grid(columnspan = 15,pady = 12)



#button
#row 1 
q = Button(root,fg = "white",text = "Q",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("Q"))
q.grid(row = 1 , column = 1)

w = Button(root,fg = "white",text = "W",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("W"))
w.grid(row = 1 , column = 2)

e = Button(root,fg = "white",text = "E",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("E"))
e.grid(row = 1 , column = 3,padx = 10,pady = 10)

r = Button(root,fg = "white",text = "R",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("R"))
r.grid(row = 1 , column = 4,padx = 10,pady = 10)

t = Button(root,fg = "white",text = "T",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("T"))
t.grid(row = 1 , column = 5,padx = 10,pady = 10)

y = Button(root,fg = "white",text = "Y",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("Y"))
y.grid(row = 1 , column = 6,padx = 10,pady = 10)

u = Button(root,fg = "white",text = "U",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("U"))
u.grid(row = 1 , column = 7,padx = 10,pady = 10)

i = Button(root,fg = "white",text = "I",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("I"))
i.grid(row = 1 , column = 8,padx = 10,pady = 10)

o = Button(root,fg = "white",text = "O",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("O"))
o.grid(row = 1 , column = 9,padx = 10,pady = 10)

p = Button(root,fg = "white",text = "P",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("P"))
p.grid(row = 1 , column = 10,padx = 10,pady = 10)

brace1 = Button(root,fg = "white",text = "{",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("{"))
brace1.grid(row = 1 , column = 11,padx = 10,pady = 10)

brace2 = Button(root,fg = "white",text = "}",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("}"))
brace2.grid(row = 1 , column = 12,padx = 10,pady = 10)

clear = Button(root,fg = "white",text = "Clear",height = 2 ,width = 10,font = "Helvetica",bg = "grey36",command =clear)
clear.grid(row = 1 , column = 13,padx = 10,pady = 10)

#row 2

a = Button(root,fg = "white",text = "A",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("A"))
a.grid(row = 2 , column = 1,padx = 10,pady = 10)

s = Button(root,fg = "white",text = "S",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("S"))
s.grid(row = 2 , column = 2,padx = 10,pady = 10)

d = Button(root,fg = "white",text = "D",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("D"))
d.grid(row = 2 , column = 3,padx = 10,pady = 10)

f = Button(root,fg = "white",text = "F",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("F"))
f.grid(row = 2 , column = 4,padx = 10,pady = 10)

g = Button(root,fg = "white",text = "G",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("G"))
g.grid(row = 2 , column = 5,padx = 10,pady = 10)

h = Button(root,fg = "white",text = "H",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("H"))
h.grid(row = 2 , column = 6,padx = 10,pady = 10)

j = Button(root,fg = "white",text = "J",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("J"))
j.grid(row = 2 , column = 7,padx = 10,pady = 10)

k = Button(root,fg = "white",text = "K",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("K"))
k.grid(row = 2 , column = 8,padx = 10,pady = 10)

l = Button(root,fg = "white",text = "L",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("L"))
l.grid(row = 2 , column = 9,padx = 10,pady = 10)

semicol= Button(root,fg = "white",text = ";",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button(";"))
semicol.grid(row = 2 , column = 10,padx = 10,pady = 10)

diq = Button(root,fg = "white",text = "'",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button(""))
diq.grid(row = 2 , column = 11,padx = 10,pady = 10)

enter = Button(root,fg = "white",text = "Enter",height = 2 ,width = 15,font = "Helvetica",bg = "grey36",command = lambda : button(""))
enter.grid(row = 2 , column = 12,padx = 10,pady = 10,columnspan = 2)

#row 3

z = Button(root,fg = "white",text = "Z",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("Z"))
z.grid(row = 3 , column = 1,padx = 10,pady = 10)

x = Button(root,fg = "white",text = "X",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("X"))
x.grid(row = 3 , column = 2,padx = 10,pady = 10)

c = Button(root,fg = "white",text = "C",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("C"))
c.grid(row = 3 , column = 3,padx = 10,pady = 10)

v = Button(root,fg = "white",text = "V",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("V"))
v.grid(row = 3 , column = 4,padx = 10,pady = 10)

b = Button(root,fg = "white",text = "B",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("B"))
b.grid(row = 3 , column = 5,padx = 10,pady = 10)

n = Button(root,fg = "white",text = "N",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("N"))
n.grid(row = 3 , column = 6,padx = 10,pady = 10)

m = Button(root,fg = "white",text = "M",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("M"))
m.grid(row = 3 , column = 7,padx = 10,pady = 10)

arrow1 = Button(root,fg = "white",text = "<",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("<"))
arrow1.grid(row = 3 , column = 8,padx = 10,pady = 10)

arrow2 = Button(root,fg = "white",text = ">",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button(">"))
arrow2.grid(row = 3 , column = 9,padx = 10,pady = 10)

slash = Button(root,fg = "white",text = "/",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("/"))
slash.grid(row = 3 , column = 10,padx = 10,pady = 10)

ques = Button(root,fg = "white",text = "?",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("?"))
ques.grid(row = 3 , column = 11,padx = 10,pady = 10)

comma = Button(root,fg = "white",text = ",",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button(","))
comma.grid(row = 3 , column = 12,padx = 10,pady = 10)

dot = Button(root,fg = "white",text = ".",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("."))
dot.grid(row = 3 , column = 13,padx = 10,pady = 10)

#row4

ctrl = Button(root,fg = "white",text = "Ctrl",height = 2 ,width = 5,font = "Helvetica",bg = "grey36")
ctrl.grid(row = 4 , column = 1,padx = 10,pady = 10)

fn = Button(root,fg = "white",text = "Fn",height = 2 ,width = 5,font = "Helvetica",bg = "grey36")
fn.grid(row = 4 , column = 2,padx = 10,pady = 10)

win = Button(root,fg = "white",text = "⊞",height = 2 ,width = 5,font = "Helvetica",bg = "grey36")
win.grid(row = 4 , column = 3,padx = 10,pady = 10)

alt = Button(root,fg = "white",text = "Alt",height = 2 ,width = 5,font = "Helvetica",bg = "grey36")
alt.grid(row = 4 , column = 4,padx = 10,pady = 10)

space = Button(root,fg = "white" , height = 2 ,width = 30,font = "Helvetica",bg = "grey36",command = lambda : button(" "))
space.grid(row = 4 , column = 5,padx = 10,pady = 10,columnspan = 4)

brac1 = Button(root,fg = "white",text = "(",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button("("))
brac1.grid(row = 4 , column = 9,padx = 10,pady = 10)

brac2 = Button(root,fg = "white",text = ")",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = lambda : button(")"))
brac2.grid(row = 4 , column = 10,padx = 10,pady = 10)

arrow1= Button(root,fg = "white",text = "<",height = 2 ,width = 5,font = "Helvetica",bg = "grey36")
arrow1.grid(row = 4 , column = 11,padx = 10,pady = 10)

arrow2 = Button(root,fg = "white",text = ">",height = 2 ,width = 5,font = "Helvetica",bg = "grey36")
arrow2.grid(row = 4 , column = 12,padx = 10,pady = 10)

bs = Button(root,fg = "white",text = "<]",height = 2 ,width = 5,font = "Helvetica",bg = "grey36",command = backspace )
bs.grid(row = 4 , column = 13,padx = 10,pady = 10)

root.mainloop()
              
