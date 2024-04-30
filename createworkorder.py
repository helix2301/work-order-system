from tkinter import *
from databases import Database
import sys
import sqlite3
import random
import os
from tkinter import ttk

def quit():
    sys.exit()

def add():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR + '\\store.db')
    my_conn = sqlite3.connect(db_path)
    status = clicked.get()
    priority = clicked2.get()
    CN = comboBox.get()
    FN = FN_text.get()
    LN = LN_text.get()
    des = des_text.get()
    email = email_text.get()
    phone = phone_text.get()
    num = value
    my_data=(status, priority, CN, FN, LN, phone, email, des, num)
    my_query="INSERT INTO workorders VALUES (?,?,?,?,?,?,?,?,?,null,null)"
    my_conn.execute(my_query,my_data)
    my_conn.commit()
    CN_entry.delete(0, 255)
    FN_entry.delete(0, 255)
    LN_entry.delete(0, 255)
    phone_entry.delete(0, 255)
    email_entry.delete(0, 255)
    des_entry.delete(0, 255)
    clicked.set("New Request")
    clicked2.set("Select Priority")
    sys.exit()

#create window

app = Tk()
  
# Dropdown menu options
options = [
    "New Request",
    "In Progress",
    "On Hold",
    "Completed",
]
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( "New Request" )
  
# Create Dropdown menu
drop = OptionMenu( app , clicked , *options )
drop.pack()
drop.grid(row=0, column=1, padx=10, pady=10)

FN_label = Label(app, text='Status:', font=('bold', 14))
FN_label.grid(row=0, column=0, sticky=W)

# Dropdown menu options
options2 = [
    "Urgent",
    "High",
    "Medium",
    "Low",
]
  
# datatype of menu text
clicked2 = StringVar()
  
# initial menu text
clicked2.set( "Select Priority" )
  
# Create Dropdown menu
drop2 = OptionMenu( app , clicked2 , *options2 )
drop2.grid(row=1, column=1, padx=10, pady=10)

LN_label = Label(app, text='Priority:', font=('bold', 14))
LN_label.grid(row=1, column=0, sticky=W)

CN_text = StringVar()
CN_label = Label(app, text='Company Name:', font=('bold', 14))
CN_label.grid(row=2, column=0, sticky=W)
CN_entry = Entry(app, textvariable=CN_text, width=30)
#CN_entry.grid(row=2, column=1, padx=10, pady=10)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR + '\\store.db')
my_conn = sqlite3.connect(db_path)
curs = my_conn.cursor()
curs.execute('select CN from customers;')
results = curs.fetchall()
curs.close()
my_conn.close()
results_for_combobox = [result[0] for result in results]
comboBox = ttk.Combobox(app,values=results_for_combobox)
comboBox.grid(row=2, column=1, padx=10, pady=10)
#clicked3 = StringVar(app, results_for_combobox)


FN_text = StringVar()
FN_label = Label(app, text='First Name:', font=('bold', 14))
FN_label.grid(row=3, column=0, sticky=W)
FN_entry = Entry(app, textvariable=FN_text, width=30)
FN_entry.grid(row=3, column=1, padx=10, pady=10)

LN_text = StringVar()
LN_label = Label(app, text='Last Name:', font=('bold', 14))
LN_label.grid(row=4, column=0, sticky=W)
LN_entry = Entry(app, textvariable=LN_text, width=30)
LN_entry.grid(row=4, column=1, padx=10, pady=10)

phone_text = StringVar()
phone_label = Label(app, text='Phone:(Numbers Only)', font=('bold', 14))
phone_label.grid(row=5, column=0, sticky=W)
phone_entry = Entry(app, textvariable=phone_text, width=30)
phone_entry.grid(row=5, column=1, padx=10, pady=10)

email_text = StringVar()
email_label = Label(app, text='Email:', font=('bold', 14))
email_label.grid(row=6, column=0, sticky=W)
email_entry = Entry(app, textvariable=email_text, width=30)
email_entry.grid(row=6, column=1, padx=10, pady=10)

value = random.randint(1,1000)
num_text = int(value)
num_label = Label(app, text='Word Order Number:', font=('bold', 14))
num_label.grid(row=7, column=0, sticky=W)
num_entry_label = Label(app, text=(num_text), width=30, font=('bold', 14))
num_entry_label.grid(row=7, column=1, padx=10, pady=10)

des_text = StringVar()
des_label = Label(app, text='Description:', font=('bold', 14))
des_label.grid(row=8, column=0, sticky=W)
des_entry = Entry(app, textvariable=des_text, width=50)
des_entry.grid(row=8, column=1, padx=10, pady=10)

add_btn = Button(app, text='Add', width=12, command=add)
add_btn.grid(row=10, column=0, padx=10, pady=10)

remove_btn = Button(app, text='Close', width=12, command=quit)
remove_btn.grid(row=10, column=1, padx=10, pady=10)


app.title('New Work Order')
app.geometry('525x435')

#start program
app.mainloop()