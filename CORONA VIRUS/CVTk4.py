from tkinter import *
from tkinter import messagebox as tmsg

def module_three():
    window_three = Toplevel()
    window_three.geometry("700x200")
    window_three.config(bg="navajo white")
    window_three.title("Corona Virus Detector")
    window_three.iconbitmap("C://Users//Iris//Desktop//geekforgeeks//FaceMask.ico")



    #functions
    def get_total():
        global total
        total = 0
        if chest_yes.get() == 1:
            total += 9
        elif chest_no.get() == 1:
            total += 1
        if breathing_yes.get() == 1:
            total += 9
        elif breathing_no.get() == 1:
            total += 1
        if total < 6:
            a = tmsg.showinfo("Caution", "Your answers predict that you're at medium to high risk for COVID-19, you must ensure that you must get \
yourself tested. There are chances that you could be asymtomatic, so we prefer you to visit a doctor or health-care \
center ")
            return a
        elif total > 6:
            b  = tmsg.showinfo("Caution","Your answers predict that you at a very high risk for COVID-19, you must ensure that you must get \
yourself tested within this hour. Please take this issue very seriously !")
            return b

    def close_info():
        a = tmsg.askyesno("Close", "Are you sure ?")
        if a == True:
            return window_three.destroy()
        else:
            pass

    def abouter():
        print(tmsg.showinfo("Carls software", "Hello , I am an amateur developer inspiring to become a pro. developer"))

    # menu
    close = Menu(window_three)
    close.add_command(label="Close", command=close_info)
    window_three.config(menu=close)
    close.add_command(label="About", command=abouter)

    # label
    Label(window_three, bg="navajo white").grid(column=2)
    Label(window_three, bg="navajo white").grid(row=2)

    chest_label = Label(window_three, text="1)Have you been experiencing chest pain ? ", highlightcolor="blue", padx=10,
                       pady=10,
                       bg="lavender", font="comicsans 15 bold ").grid(row=1)
    breathing_label = Label(window_three, text="2)Have you been experiencing breathing issues ?  ", highlightcolor="blue", padx=10,
                         pady=10,
                         bg="lavender", font="comicsans 15 bold ").grid(row=3)

    # variable
    chest_yes = IntVar()
    chest_no = IntVar()
    breathing_yes = IntVar()
    breathing_no = IntVar()

    # button
    chest_button_yes = Checkbutton(window_three, variable=chest_yes, text="YES", relief=RAISED, bg="lime green",
                                  font="fixedsys", padx=5, pady=5).grid(row=1, column=1)
    chest_button_no = Checkbutton(window_three, variable=chest_no, text="NO", relief=RAISED, bg="tomato", font="fixedsys",
                                 padx=5, pady=5).grid(row=1, column=3)

    breathing_button_yes = Checkbutton(window_three, variable= breathing_yes, text="YES", relief=RAISED, bg="lime green",
                                    font="fixedsys", padx=5, pady=5).grid(row=3, column=1)
    breathing_button_no = Checkbutton(window_three, variable=breathing_no, text="NO", relief=RAISED, bg="tomato",
                                   font="fixedsys",
                                   padx=5, pady=5).grid(row=3, column=3)
    button_submit = Button(window_three, text="SUBMIT", command=get_total, padx=10, pady=10).grid(row=6, column=3)


    #window_three.mainloop()
if __name__ == "__main__":
    module_three()