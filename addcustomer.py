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
    CN = CN_text.get()
    email = email_text.get()
    phone = phone_text.get()
    address = address_text.get()
    city = city_text.get()
    state = state_text.get()
    zip = zip_text.get()
    country = country_text.get()
    my_data=(FN, LN, CN, email, phone, address, city, state, zip, country)
    my_query="INSERT INTO customers VALUES (NULL,?,?,?,?,?,?,?,?,?,?)"
    my_conn.execute(my_query,my_data)
    my_conn.commit()
    FN_entry.delete(0, 255)
    LN_entry.delete(0, 255)
    CN_entry.delete(0, 255)
    email_entry.delete(0, 255)
    phone_entry.delete(0, 255)
    address_entry.delete(0, 255)
    city_entry.delete(0, 255)
    state_entry.delete(0, 255)
    zip_entry.delete(0, 255)
    country_entry.delete(0, 255)


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

CN_text = StringVar()
CN_label = Label(app, text='Company Name:', font=('bold', 10))
CN_label.grid(row=2, column=0, sticky=W)
CN_entry = Entry(app, textvariable=CN_text, width=50)
CN_entry.grid(row=2, column=1, padx=10, pady=10)

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

address_text = StringVar()
address_label = Label(app, text='Address:', font=('bold', 10))
address_label.grid(row=5, column=0, sticky=W)
address_entry = Entry(app, textvariable=address_text, width=50)
address_entry.grid(row=5, column=1, padx=10, pady=10)

city_text = StringVar()
city_label = Label(app, text='City:', font=('bold', 10))
city_label.grid(row=6, column=0, sticky=W)
city_entry = Entry(app, textvariable=city_text, width=50)
city_entry.grid(row=6, column=1, padx=10, pady=10)

state_text = StringVar()
state_label = Label(app, text='State:', font=('bold', 10))
state_label.grid(row=7, column=0, sticky=W)
state_entry = Entry(app, textvariable=state_text, width=50)
state_entry.grid(row=7, column=1, padx=10, pady=10)

zip_text = StringVar()
zip_label = Label(app, text='Zip:', font=('bold', 10))
zip_label.grid(row=8, column=0, sticky=W)
zip_entry = Entry(app, textvariable=zip_text, width=50)
zip_entry.grid(row=8, column=1, padx=10, pady=10)

country_text = StringVar()
country_label = Label(app, text='Country:', font=('bold', 10))
country_label.grid(row=9, column=0, sticky=W)
country_entry = Entry(app, textvariable=country_text, width=50)
country_entry.grid(row=9, column=1, padx=10, pady=10)

add_btn = Button(app, text='Add', width=12, command=add, font=('bold', 10))
add_btn.grid(row=10, column=0, padx=10, pady=10)

remove_btn = Button(app, text='Close', width=12, command=quit, font=('bold', 10))
remove_btn.grid(row=10, column=1, padx=10, pady=10)


app.title('Add Customer')
app.geometry('500x475')

#start program
app.mainloop()

#https://www.plus2net.com/python/tkinter-sqlite-insert.php
#https://github.com/TomSchimansky/CustomTkinter/wiki