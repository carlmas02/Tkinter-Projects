import pyttsx3
import CVTk3
from tkinter import *
from tkinter import messagebox as tmsg

#code for tts

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
volume = engine.getProperty('volume')
print (volume)
engine.setProperty('volume',0.5)
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 175)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def module_one():
    #main root
    window_one = Toplevel()
    window_one.geometry("700x500")
    window_one.config(bg = "navajo white")
    window_one.iconbitmap("C://Users//Iris//Desktop//geekforgeeks//FaceMask.ico")
    #window_one.minsize(height = 600 ,width=900)
    #window_one.maxsize(height = 600 ,width=900)
    window_one.title("Corona Virus Detector")

    #detector function
    def detector():
        if total < 24:
            speak(
                "Your answers predict that you are at a low-risk for COVID-19, you must ensure you protect yourself and "
                " ensure you follow social distancing norms. ")
            tmsg.showinfo("Success",
                          "Your answers predict that you are at a low-risk for COVID-19, you must ensure you protect yourself and "
                          " ensure you follow social distancing norms. ")


        elif total > 25:
            window_one.destroy()
            CVTk3.module_two()

    #functions

    def error_func():
        if fever_yes.get() == 0 and fever_no.get() == 0 and cough_yes.get() ==0 and cough_no.get() and fatigue_yes.get()\
                == 0 and fatigue_no.get()== 0 and body_yes.get()==0 and body_no.get()== 0 and app_yes.get()== 0 and \
            app_no.get() == 0 :
            tmsg.showinfo("Error","ya")
        elif fever_yes.get() == 1 and fever_no.get() == 1:
            tmsg.showinfo("Error!", "Please choose a single option. ")
        elif cough_yes.get() == 1 and cough_no.get() == 1:
            tmsg.showinfo("Error!", "Please choose a single option. ")
        elif fatigue_yes.get() == 1 and fatigue_no.get() == 1:
            tmsg.showinfo("Error!", "Please choose a single option. ")
        elif body_yes.get() == 1 and body_no.get() == 1:
            tmsg.showinfo("Error!", "Please choose a single option. ")
        elif app_yes.get() == 1 and app_no.get() == 1:
            tmsg.showinfo("Error!", "Please choose a single option. ")



    def close_info():
        a = tmsg.askyesno("Close","Are you sure ?")
        if a == True:
            return window_one.destroy()
        else :
            pass

    def abouter():
        print(tmsg.showinfo("Carls software", "Hello , I am an amateur developer inspiring to become a pro. developer"))

    def get_total():
        global total
        total = 0
        if fever_yes.get() == 1:
            total += 4
        elif fever_no.get() == 1 :
            pass
        if cough_yes.get() == 1:
            total += 6
        elif cough_no.get() == 1:
            pass
        if fatigue_yes.get() == 1:
            total += 7
        elif fatigue_no.get() == 1 :
            pass
        if app_yes.get() == 1 :
            total += 7
        elif app_no.get() == 1 :
            pass
        if body_yes.get() == 1 :
            total += 8
        elif body_no.get() == 1  :
            pass
        print(total)
        detector()



    button_submit = Button(window_one,text ="SUBMIT" ,command = get_total , padx = 10 , pady = 10 ).grid(row = 12 ,column = 3)


    #menu
    close = Menu(window_one)
    close.add_command(label = "Close" ,command = close_info )
    window_one.config(menu = close )
    close.add_command(label = "About" ,command = abouter )

    #labelframe
    be = LabelFrame(window_one,padx = 10, pady = 10).grid()



    #label
    Label(window_one,bg = "navajo white").grid(column = 2)
    Label(window_one, bg="navajo white").grid(row = 2)
    Label(window_one, bg="navajo white").grid(row=4)
    Label(window_one, bg="navajo white").grid(row=6)
    Label(window_one, bg="navajo white").grid(row=8)
    Label(window_one, bg="navajo white").grid(row=10)


    label_1 = Label(window_one,text = "Welcome !!!" ,padx = 10 ,pady = 10 ,bg = "navajo white",font = "Helvetica 16 italic").grid(row = 0)

    age_label = Label(window_one,text = "1)What is your age ? " , highlightcolor= "blue" ,padx = 10 ,pady = 10 ,
    bg = "lavender", font = "comicsans 15 bold ").grid(row =1)
    fever_label = Label(window_one, text="2)Have you been having fever recently ? ", highlightcolor="blue", padx=10, pady=10,
    bg="lavender", font="comicsans 15 bold ").grid(row=3)
    cough_label = Label(window_one , text="3)Have you been having coughing recently ? ", highlightcolor="blue", padx=10, pady=10,
    bg="lavender", font="comicsans 15 bold ").grid(row=5)
    fatigue_label =Label(window_one , text="4)Have you been feeling tired recently ? ", highlightcolor="blue", padx=10, pady=10,
    bg="lavender", font="comicsans 15 bold ").grid(row=7)
    appetite_label = Label(window_one, text="5)have you lost your appetite to eat ? ", highlightcolor="blue", padx=10,
    pady=10, bg="lavender", font="comicsans 15 bold ").grid(row=9)
    body_label = Label(window_one, text="6)have you been having body pain ? ", highlightcolor="blue", padx=10,
                           pady=10, bg="lavender", font="comicsans 15 bold ").grid(row=11)

    #intvar
    age_yes = StringVar()
    fever_yes = IntVar()
    fever_no = IntVar()
    cough_yes = IntVar()
    cough_no = IntVar()
    fatigue_yes = IntVar()
    fatigue_no = IntVar()
    app_yes  = IntVar()
    app_no = IntVar()
    body_yes = IntVar()
    body_no  = IntVar()



    #button
    age_entry = Entry(window_one,textvariable = age_yes ,text = "YES" ,relief = RAISED, bg = "light grey" ,font = "fixedsys").grid(row =1 , column = 1)

    fever_button_yes = Checkbutton(window_one,variable = fever_yes, text="YES", relief=RAISED, bg="lime green", font="fixedsys", padx=5, pady=5).grid(row=3, column=1)
    fever_button_no = Checkbutton(window_one,variable = fever_no, text="NO", relief=RAISED, bg="tomato", font="fixedsys", padx=5, pady=5).grid(row=3, column=3)

    cough_button_yes = Checkbutton(window_one,variable = cough_yes, text="YES", relief=RAISED, bg="lime green", font="fixedsys", padx=5,pady=5).grid(row=5, column=1)
    cough_button_no = Checkbutton(window_one,variable = cough_no, text="NO", relief=RAISED, bg="tomato", font="fixedsys", padx=5, pady=5).grid(row=5, column=3)

    fatigue_button_yes = Checkbutton(window_one,variable = fatigue_yes, text="YES", relief=RAISED, bg="lime green", font="fixedsys", padx=5, pady=5).grid(row=7, column=1)
    fatigue_button_no = Checkbutton(window_one,variable = fatigue_no, text="NO", relief=RAISED, bg="tomato", font="fixedsys", padx=5, pady=5).grid(row=7, column=3)

    appetite_button_yes = Checkbutton(window_one,variable = app_yes, text="YES", relief=RAISED, bg="lime green", font="fixedsys", padx=5, pady=5).grid(row=9, column=1)
    appetite_button_no = Checkbutton(window_one,variable = app_no, text="NO", relief=RAISED, bg="tomato", font="fixedsys", padx=5, pady=5).grid(row=9, column=3)

    body_button_yes = Checkbutton(window_one,variable = body_yes, text="YES", relief=RAISED, bg="lime green", font="fixedsys", padx=5,pady=5).grid(row=11, column=1)
    body_button_no = Checkbutton(window_one,variable = body_no, text="NO", relief=RAISED, bg="tomato", font="fixedsys", padx=5,pady=5).grid(row=11, column=3)


if __name__ == "__main__":
    module_one()

