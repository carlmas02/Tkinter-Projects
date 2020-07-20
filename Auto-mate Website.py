from tkinter import *
import webbrowser

root = Tk()

root.title("AUTO-WEBSITE")
root.geometry("550x500")
root.configure(bg = "aquamarine")

root.minsize(height = 550, width = 550)

#canvas  not needed bcoz we can use configure
#canvas_widget = Canvas(root, width = 550 , height = 550, bg = "navajo white")

#functions
def openweb():
    if web.get() == 1:
        webbrowser.open('http://spotify.com')
    else :
        pass



#frame
frame_1 = Frame(root, bg = "red", borderwidth = 8 )
frame_2 = Frame(root, bg = "red", borderwidth = 4 )



#labels
header = Label(frame_1 ,text = "We Help You Access Your Favourite Websites ASAP!!!",font = "comicsans 15 bold",relief =
               GROOVE, padx = 5)
#variable
web = IntVar()

#buttons
button1 = Checkbutton(frame_2,text = "SPOTIFY", variable = web)

button2 = Button(text = "CLICK HERE" , command = openweb)

#.grid()
header.pack()
frame_1.pack()
frame_2.pack()
button1.pack()
button2.pack()





root.mainloop()