from tkinter import *
import sqlite3

root = Tk()


root.geometry("240x120")
root.title("TKINTER SQL")

def sub():
    #create connectiion for db
    conn = sqlite3.connect("my.db")
    c = conn.cursor()
    #c.execute("create TABLE address(name TEXT)")
    
    #insert
    c.execute("INSERT INTO address VALUES(:name)",
              {
                  'name': name_entry.get()

              })
     
    
    conn.commit()
    conn.close()

    name_entry.delete(0,END)

def query():
    conn = sqlite3.connect("my.db")
    c = conn.cursor()

    #query db
    c.execute("SELECT *, oid FROM address")
    a = c.fetchall()
    print(a)
    
    
    
    conn.commit()
    conn.close()

    cam = ''
    for i in a :
        cam +=  str(i[0]) + '\n'
        
    Label(root,text = cam ).grid()
       

#label
name_label = Label(root,text = "name")
name_label.grid()


#entry
name_entry =  Entry(root)
name_entry.grid()


#button
submit = Button(root,text = "Press",command = sub)
submit.grid()

qu = Button(root,text = "show",command = query)
qu.grid()


root.mainloop()

          





              


              

