from tkinter import *
from webbrowser import get
from databases import Database
import sys
import sqlite3
import os
import subprocess
from tkinter import ttk
from tkinter import messagebox

### get PDF file libraries  
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import  A4

my_conn = sqlite3.connect('store.db')

#create window

app = Tk()

ST_text = StringVar()
ST_label = Label(app, text='Status:', font=('bold', 14))
ST_label.grid(row=0, column=0, sticky=W)
ST_entry = Entry(app, textvariable=ST_text, width=50)
ST_entry.grid(row=0, column=1, padx=10, pady=10)

PR_text = StringVar()
PR_label = Label(app, text='Priority:', font=('bold', 14))
PR_label.grid(row=1, column=0, sticky=W)
PR_entry = Entry(app, textvariable=PR_text, width=50)
PR_entry.grid(row=1, column=1, padx=10, pady=10)

CN_text = StringVar()
CN_label = Label(app, text='Company Name:', font=('bold', 14))
CN_label.grid(row=2, column=0, sticky=W)
CN_entry = Entry(app, textvariable=CN_text, width=50)
CN_entry.grid(row=2, column=1, padx=10, pady=10)

FN_text = StringVar()
FN_label = Label(app, text='First Name:', font=('bold', 14))
FN_label.grid(row=3, column=0, sticky=W)
FN_entry = Entry(app, textvariable=FN_text, width=50)
FN_entry.grid(row=3, column=1, padx=10, pady=10)

LN_text = StringVar()
LN_label = Label(app, text='Last Name:', font=('bold', 14))
LN_label.grid(row=4, column=0, sticky=W)
LN_entry = Entry(app, textvariable=LN_text, width=50)
LN_entry.grid(row=4, column=1, padx=10, pady=10)

phone_text = StringVar()
phone_label = Label(app, text='Phone:', font=('bold', 14))
phone_label.grid(row=5, column=0, sticky=W)
phone_entry = Entry(app, textvariable=phone_text, width=50)
phone_entry.grid(row=5, column=1, padx=10, pady=10)

email_text = StringVar()
email_label = Label(app, text='email:', font=('bold', 14))
email_label.grid(row=6, column=0, sticky=W)
email_entry = Entry(app, textvariable=email_text, width=50)
email_entry.grid(row=6, column=1, padx=10, pady=10)

des_text = StringVar()
des_label = Label(app, text='Description:', font=('bold', 14))
des_label.grid(row=7, column=0, sticky=W)
des_entry = Entry(app, textvariable=des_text, width=50)
des_entry.grid(row=7, column=1, padx=10, pady=10)

res_text = StringVar()
res_label = Label(app, text='Resolved:', font=('bold', 14))
res_label.grid(row=8, column=0, sticky=W)
res_entry = Entry(app, textvariable=res_text, width=50)
res_entry.grid(row=8, column=1, padx=10, pady=10)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR + '\\store.db')
my_conn = sqlite3.connect(db_path)
curs = my_conn.cursor()
curs.execute('select WordOrdernum from workorders;')
results = curs.fetchall()
curs.close()
my_conn.close()
results_for_combobox = [result[0] for result in results]
comboBox = ttk.Combobox(app,values=results_for_combobox)
comboBox.grid(row=9, column=1, padx=10, pady=10)

wo_text = StringVar()
wo_label = Label(app, text='work order#:', font=('bold', 14))
wo_label.grid(row=9, column=0, sticky=W)
wo_entry = Entry(app, textvariable=wo_text, width=20)
#wo_entry.grid(row=9, column=1, padx=10, pady=10)

def getrecord():
    record_id = comboBox.get()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR + '\\store.db')
    my_conn = sqlite3.connect(db_path)
    cursor = my_conn.cursor()
    cursor.execute("select * from workorders where WordOrdernum = " + record_id)
    records = cursor.fetchall

    for record in records():
        ST_entry.insert(END, record[0])
        PR_entry.insert(END, record[1])
        CN_entry.insert(END, record[2])
        FN_entry.insert(END, record[3])
        LN_entry.insert(END, record[4])
        phone_entry.insert(END, record[5])
        email_entry.insert(END, record[6])
        des_entry.insert(END, record[7])

def print():
    status = ST_entry.get()
    priority = PR_entry.get()
    CN = CN_text.get()
    FN = FN_text.get()
    LN = LN_text.get()
    des = des_text.get()
    email = email_text.get()
    phone = phone_text.get()
    num = wo_text.get()
    #create PDF file
    pdf_name = ("Work Order" + str(num) + ".pdf")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    save_name = os.path.join(BASE_DIR, "reports", pdf_name)
    c = canvas.Canvas(save_name, pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(30,750,"Status: " + status)
    c.drawString(30,730,"Priority: " + priority)
    c.drawString(30,710,"Company Name: " + CN)
    c.drawString(30,690,"First Name: " + FN)
    c.drawString(30,670,"Last Name: " + LN)
    c.drawString(30,650,"Phone: " + phone)
    c.drawString(30,630,"Email: " + email)
    c.drawString(30,610,"Description: " + des)
    c.drawString(30,590,"Word Order Number: " + str(num))
    c.showPage()
    c.save()
    os.startfile(os.path.join(BASE_DIR, "reports", pdf_name))


add_btn = Button(app, text='Get Work Order', width=12, command=getrecord)
add_btn.grid(row=10, column=0, padx=10, pady=10)

cl_btn = Button(app, text='Print', width=12, command=print)
cl_btn.grid(row=10, column=1, padx=10, pady=10)

app.title('Print Work Order')
app.geometry('500x475')

#start program
app.mainloop()
