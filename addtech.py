from tkinter import *
from tkinter import ttk
import sys
import sqlite3
import os
import tkinter
from tkinter import StringVar
from sqlite3 import *
from sqlite3.dbapi2 import *

def quit():
    sys.exit()

def add():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR + '\\store.db')
    my_conn = sqlite3.connect(db_path)
    FN = FN_text.get()
    LN = LN_text.get()
    email = email_text.get()
    phone = phone_text.get()
    my_data=(FN, LN, email, phone)
    my_query="INSERT INTO techs VALUES (?,?,?,?)"
    my_conn.execute(my_query,my_data)
    my_conn.commit()
    FN_entry.delete(0, 255)
    LN_entry.delete(0, 255)
    email_entry.delete(0, 255)
    phone_entry.delete(0, 255)
    sys.exit()

#create window

app = Tk()

FN_text = StringVar()
FN_label = Label(app, text='First Name:', font=('bold', 10))
FN_label.grid(row=0, column=0, sticky=W)
FN_entry = Entry(app, textvariable=FN_text, width=50)
FN_entry.grid(row=0, column=1, padx=10, pady=10)

LN_text = StringVar()
LN_label = Label(app, text='Last Name:', font=('bold', 10))
LN_label.grid(row=1, column=0, sticky=W)
LN_entry = Entry(app, textvariable=LN_text, width=50)
LN_entry.grid(row=1, column=1, padx=10, pady=10)

email_text = StringVar()
email_label = Label(app, text='E-mail:', font=('bold', 10))
email_label.grid(row=3, column=0, sticky=W)
email_entry = Entry(app, textvariable=email_text, width=50)
email_entry.grid(row=3, column=1, padx=10, pady=10)

phone_text = StringVar()
phone_label = Label(app, text='Phone:(Numbers Only)', font=('bold', 10))
phone_label.grid(row=4, column=0, sticky=W)
phone_entry = Entry(app, textvariable=phone_text, width=50)
phone_entry.grid(row=4, column=1, padx=10, pady=10)

add_btn = Button(app, text='Add', width=12, command=add, font=('bold', 10))
add_btn.grid(row=10, column=0, padx=10, pady=10)

remove_btn = Button(app, text='Close', width=12, command=quit, font=('bold', 10))
remove_btn.grid(row=10, column=1, padx=10, pady=10)

app.title('Add Tech')
app.geometry('475x225')

#start program
app.mainloop()

#https://www.plus2net.com/python/tkinter-sqlite-insert.php
#https://github.com/TomSchimansky/CustomTkinter/wiki