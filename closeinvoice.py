from tkinter import *
from databases import Database
import sys
import sqlite3
import os
import subprocess
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

#create window

app = Tk()

invoice_text = StringVar()
invoice_label = Label(app, text='Invoice Number:', font=('bold', 14))
invoice_label.grid(row=1, column=0, sticky=W)
#invoice_entry = Entry(app, textvariable=invoice_text, width=10)
#invoice_entry.grid(row=2, column=1, padx=10, pady=10)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR + '\\store.db')
my_conn = sqlite3.connect(db_path)
curs = my_conn.cursor()
curs.execute("select InvoiceNumber from invoices where Paid is null")
results = curs.fetchall()
curs.close()
my_conn.close()
results_for_combobox = [result[0] for result in results]
comboBox = ttk.Combobox(app,values=results_for_combobox)
comboBox.grid(row=1, column=1, padx=10, pady=10)
#clicked3 = StringVar(app, results_for_combobox)

CN_text = StringVar()
CN_label = Label(app, text='Company Name:', font=('bold', 14))
CN_label.grid(row=2, column=0, sticky=W)
CN_entry = Entry(app, textvariable=CN_text, width=30)
CN_entry.grid(row=2, column=1, padx=10, pady=10)

cal2_text = StringVar()
cal2_label = Label(app, text='Due Date:', font=('bold', 14))
cal2_label.grid(row=3, column=0, sticky=W)
cal2_entry = Entry(app, textvariable=cal2_text, width=10)
cal2_entry.grid(row=3, column=1, padx=10, pady=10)

parts_text = StringVar()
parts_label = Label(app, text='Parts Description:', font=('bold', 14))
parts_label.grid(row=4, column=0, sticky=W)
parts_entry = Entry(app, textvariable=parts_text, width=50)
parts_entry.grid(row=4, column=1, padx=10, pady=10)

parts_price_text = StringVar()
parts_price_label = Label(app, text='Parts Price:', font=('bold', 14))
parts_price_label.grid(row=5, column=0, sticky=W)
parts_price_entry = Entry(app, textvariable=parts_price_text, width=10)
parts_price_entry.grid(row=5, column=1, padx=10, pady=10)

labor_text = StringVar()
labor_label = Label(app, text='Labor Price:', font=('bold', 14))
labor_label.grid(row=6, column=0, sticky=W)
labor_entry = Entry(app, textvariable=labor_text, width=10)
labor_entry.grid(row=6, column=1, padx=10, pady=10)

des_text = StringVar()
des_label = Label(app, text='Description:', font=('bold', 14))
des_label.grid(row=8, column=0, sticky=W)
des_entry = Entry(app, textvariable=des_text, width=50)
des_entry.grid(row=8, column=1, padx=10, pady=10)

tax_text = StringVar()
tax_label = Label(app, text='Tax:', font=('bold', 14))
tax_label.grid(row=9, column=0, sticky=W)
tax_entry = Entry(app, textvariable=tax_text, width=10)
tax_entry.grid(row=9, column=1, padx=10, pady=10)

total_text = StringVar()
total_label = Label(app, text='Total:', font=('bold', 14))
total_label.grid(row=10, column=0, sticky=W)
total_entry = Entry(app, textvariable=total_text, width=10)
total_entry.grid(row=10, column=1, padx=10, pady=10)

def quit():
    sys.exit()

def getrecord():
    CN_entry.delete(0, 255)
    cal2_entry.delete(0, 255)
    parts_entry.delete(0, 255)
    parts_price_entry.delete(0, 255)
    labor_entry.delete(0, 255)
    des_entry.delete(0, 255)
    tax_entry.delete(0, 255)
    total_entry.delete(0, 255)
    record_id = comboBox.get()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR + '\\store.db')
    my_conn = sqlite3.connect(db_path)
    cursor = my_conn.cursor()
    cursor.execute("select * from invoices where InvoiceNumber = " + record_id)
    records = cursor.fetchall

    for record in records():
        CN_entry.insert(END, record[0])
        cal2_entry.insert(END, record[3])
        parts_entry.insert(END, record[4])
        parts_price_entry.insert(END, record[5])
        labor_entry.insert(END, record[6])
        des_entry.insert(END, record[7])
        tax_entry.insert(END, record[8])
        total_entry.insert(END, record[9])

def closerecord():
    SET = "paid"
    record_id = comboBox.get()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR + '\\store.db')
    my_conn = sqlite3.connect(db_path)
    cursor = my_conn.cursor()
    cursor.execute(f"UPDATE invoices SET Paid='{SET}'where InvoiceNumber = " + record_id)
    my_conn.commit()
    sys.exit()

add_btn = Button(app, text='Get Invoice', width=12, command=getrecord)
add_btn.grid(row=12, column=0, padx=10, pady=10)

cl_btn = Button(app, text='Mark Paid', width=12, command=closerecord)
cl_btn.grid(row=12, column=1, padx=10, pady=10)

close_btn = Button(app, text='Close', width=12, command=quit)
close_btn.grid(row=13, column=1, padx=10, pady=10)

app.title('Close Invoice')
app.geometry('500x485')

#start program
app.mainloop()

#https://www.plus2net.com/python/tkinter-DateEntry.php
