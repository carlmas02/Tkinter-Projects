import CVTk4
from tkinter import *
from tkinter import messagebox as tmsg

def module_two():
    window_two = Toplevel()
    window_two.geometry("650x300")
    window_two.config(bg="navajo white")
    window_two.title("Corona Virus Detector")
    window_two.iconbitmap("C://Users//Iris//Desktop//geekforgeeks//FaceMask.ico")

    #func
    def get_total():
        global total
        total = 0
        if nose_yes.get() == 1:
            total += 5
        elif nose_no.get() == 1:
            total += 1
        if nausea_yes.get() == 1:
            total += 4
        elif nausea_no.get() == 1:
            total += 1
        if smell_yes.get() == 1:
            total += 4
        elif smell_no.get() == 1:
            pass
        print(total)
        if total < 6:
            a = tmsg.showinfo("Sucess","Your answers predict that you're at medium risk for COVID-19 ,you must ensure that you must get \
yourself tested. There are chances that you could be asymtomatic, so we prefer you to visit a doctor or health-care \
center ")
            return a
        elif total > 6:
            window_two.destroy()
            CVTk4.module_three()


    def close_info():
        a = tmsg.askyesno("Close","Are you sure ?")
        if a == True:
            return window_two.destroy()
        else :
            pass

    def abouter():
        print(tmsg.showinfo("Carls software", "Hello , I am an amateur developer inspiring to become a pro. developer"))

    # menu
    close = Menu(window_two)
    close.add_command(label="Close", command=close_info)
    window_two.config(menu=close)
    close.add_command(label="About", command=abouter)

    #label
    Label(window_two, bg="navajo white").grid(column=2)
    Label(window_two, bg="navajo white").grid(row=2)
    Label(window_two, bg="navajo white").grid(row=4)

    nose_label = Label(window_two, text="1)Have you been having a runny nose ? ", highlightcolor="blue", padx=10, pady=10,
                      bg="lavender", font="comicsans 15 bold ").grid(row=1)
    nausea_label = Label(window_two, text="2)Have you been having nausea ? ", highlightcolor="blue", padx=10,
                        pady=10,
                        bg="lavender", font="comicsans 15 bold ").grid(row=3)
    smell_label = Label(window_two, text="3)Have you been experiencing lose of smell ? ", highlightcolor="blue", padx=10,
                        pady=10,
                        bg="lavender", font="comicsans 15 bold ").grid(row=5)

    #variable
    nose_yes = IntVar()
    nose_no = IntVar()
    nausea_yes = IntVar()
    nausea_no = IntVar()
    smell_yes = IntVar()
    smell_no = IntVar()

    #button
    nose_button_yes = Checkbutton(window_two, variable=nose_yes, text="YES", relief=RAISED, bg="lime green",
                                   font="fixedsys", padx=5, pady=5).grid(row=1, column=1)
    nose_button_no = Checkbutton(window_two, variable=nose_no, text="NO", relief=RAISED, bg="tomato", font="fixedsys",
                                  padx=5, pady=5).grid(row=1, column=3)

    nausea_button_yes = Checkbutton(window_two, variable=nausea_yes, text="YES", relief=RAISED, bg="lime green",
                                   font="fixedsys", padx=5, pady=5).grid(row=3, column=1)
    nausea_button_no = Checkbutton(window_two, variable=nausea_no, text="NO", relief=RAISED, bg="tomato", font="fixedsys",
                                  padx=5, pady=5).grid(row=3, column=3)

    smell_button_yes = Checkbutton(window_two, variable=smell_yes, text="YES", relief=RAISED, bg="lime green",
                                     font="fixedsys", padx=5, pady=5).grid(row=5, column=1)
    smell_button_no = Checkbutton(window_two, variable=smell_no, text="NO", relief=RAISED, bg="tomato",
                                    font="fixedsys", padx=5, pady=5).grid(row=5, column=3)

    button_submit = Button(window_two, text="SUBMIT",command = get_total , padx=10, pady=10).grid(row=6, column=3)


if __name__ == "__main__":
    module_two()
