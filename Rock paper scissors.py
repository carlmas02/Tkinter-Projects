from tkinter import *
from tkinter import messagebox as tmsg
import random

a = ["Scissor","Rock","Paper"]
global comp
comp = random.choice(a)
print(comp)
root = Tk()

root.title("ROCK-PAPER-SCISSOR")
root.geometry("660x190")
root.minsize(height = "190", width = "660")


#functions
def rock_button():
    if comp == "Paper":
        return tmsg.showinfo("Paper","Oops! You lose :(")
    elif comp == "Scissor":
        return tmsg.showinfo("Scissor","You win :)")
    elif comp == "Rock":
        return tmsg.showinfo("Rock ", "Its a draw! ")

def paper_button():
    pass
def scissor_button():
    pass



Rock = Button(root,text = "ROCK",height  = "12", width = "30" , command = rock_button).grid()
Paper = Button(root,text = "PAPER",height  = "12", width = "30" , command = paper_button).grid(row = 0 ,column = 1)
Scissor = Button(root,text = "SCISSOR",height  = "12", width = "30", command = scissor_button).grid(row = 0 ,column = 2)

root.mainloop()