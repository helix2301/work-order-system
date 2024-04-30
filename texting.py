
from twilio.rest import Client

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

def send():
    # Your Account SID from twilio.com/console
    account_sid = ""
    # Your Auth Token from twilio.com/console
    auth_token  = ""
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+1" + number_text.get(), 
        from_="+",
        body= message_text.get())

    print(message.sid)

#create window

app = Tk()

number_text = StringVar()
number_label = Label(app, text='Phone Number:', font=('bold', 10))
number_label.grid(row=0, column=0, sticky=W)
number_entry = Entry(app, textvariable=number_text, width=50)
number_entry.grid(row=0, column=1, padx=10, pady=10)

message_text = StringVar()
message_label = Label(app, text='Message:', font=('bold', 10))
message_label.grid(row=1, column=0, sticky=W)
message_entry = Entry(app, textvariable=message_text, width=50)
message_entry.grid(row=1, column=1, padx=10, pady=10)

add_btn = Button(app, text='Send', width=12, command=send, font=('bold', 10))
add_btn.grid(row=10, column=0, padx=10, pady=10)

app.title('Texting')
app.geometry('475x150')

#start program
app.mainloop()

#https://www.plus2net.com/python/tkinter-sqlite-insert.php
#https://github.com/TomSchimansky/CustomTkinter/wiki
#https://www.twilio.com/docs/libraries/python
