import CVTk2
from tkinter import *
from tkinter import messagebox as tmsg
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


#main root
root = Tk()
root.geometry("600x200")
root.config(bg = "yellow")
root.iconbitmap("C://Users//Iris//Desktop//geekforgeeks//FaceMask.ico")
root.minsize(height = 200 ,width=600)
root.maxsize(height = 200 ,width=600)
root.title("Corona Virus Detector")

#function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def new_window():
    #main
    name = nameenter.get()
    speak("Welcome" + name)
    CVTk2.module_one()


#frame W1
frame = Frame(root, bg = "red", borderwidth = 8 ,padx = 10 ,pady = 10 ).grid()

#icon
photo = PhotoImage(file="C://Users//Iris//Desktop//geekforgeeks//coronaimg.png")


#label for W1
Welcome_text = Label(frame ,text = "Welcome , please enter your name : ",font = "comicsans 15 bold", relief = GROOVE,
                     padx = 10).grid()
seperator = Label(root, bg = "yellow").grid(row =1 , column =1)

photo_label = Label(image = photo ,anchor = "s").grid(row = 2 ,column = 2)

#variable
nameenter = StringVar()

#entry for W1
name_entry = Entry(root, relief = RAISED ,textvariable = nameenter ).grid(row = 1 , column =2 )

#button for W1
enter_button = Button(frame, text = "CLICK HERE", command = new_window ,padx = 5 , pady = 5 ,bg = "navajo white").grid(row = 1, column = 4)


root.mainloop()

