from tkinter import *
from tkinter import ttk
import sys
import sqlite3
import os
import tkinter
from tkinter import StringVar
from sqlite3 import *
from sqlite3.dbapi2 import *
import stripe
import sys
from tkinter import messagebox

def quit():
    sys.exit()

def payment():
    SET = "paid"
    record_id = comboBox.get()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR + '\\store.db')
    my_conn = sqlite3.connect(db_path)
    cursor = my_conn.cursor()
    cursor.execute(f"UPDATE invoices SET Paid='{SET}'where InvoiceNumber = " + record_id)
    my_conn.commit()
    get = number_text.get()
    get1 = float(get)
    get2 = get1 * 100
    get3 = int(get2)
    card = card_text.get()
    exp_month = ex_month_text.get()
    exp_year = ex_year_text.get()
    cvc = cvc_text.get()
    stripe.api_key = "Api key goes here"
    stripe.PaymentMethod.create(
        type="card",
        card={
            "number": card,
            "exp_month": exp_month,
            "exp_year": exp_year,
            "cvc": cvc,
            },)
    charge = stripe.Charge.create(
        amount=get3,
        currency="usd",
        description= "payment for work order",
        source=  stripe.Token.create(
        card={
            "number": card,
            "exp_month": exp_month,
            "exp_year": exp_year,
            "cvc": cvc,
        },),      
            )
    messagebox.showinfo('Success', 'Payment Successful') 

def getrecord():
    number_entry.delete(0, 255)
    record_id = comboBox.get()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR + '\\store.db')
    my_conn = sqlite3.connect(db_path)
    cursor = my_conn.cursor()
    cursor.execute("select * from invoices where InvoiceNumber = " + record_id)
    records = cursor.fetchall

    for record in records():
        number_entry.insert(END, record[9])

app = Tk()

card_text = StringVar()
card_label = Label(app, text='Card #:', font=('bold', 10))
card_label.grid(row=0, column=0, sticky=W)
card_entry = Entry(app, textvariable=card_text, width=16)
card_entry.grid(row=0, column=1, padx=10, pady=10)

ex_month_text = StringVar()
ex_month_label = Label(app, text='Exp Month:(number)', font=('bold', 10))
ex_month_label.grid(row=1, column=0, sticky=W)
ex_month_entry = Entry(app, textvariable=ex_month_text, width=2)
ex_month_entry.grid(row=1, column=1, padx=10, pady=10)

ex_year_text = StringVar()
ex_year_label = Label(app, text='Exp Year:', font=('bold', 10))
ex_year_label.grid(row=2, column=0, sticky=W)
ex_year_entry = Entry(app, textvariable=ex_year_text, width=4)
ex_year_entry.grid(row=2, column=1, padx=10, pady=10)

cvc_text = StringVar()
cvc_label = Label(app, text='CVC:', font=('bold', 10))
cvc_label.grid(row=3, column=0, sticky=W)
cvc_entry = Entry(app, textvariable=cvc_text, width=4)
cvc_entry.grid(row=3, column=1, padx=10, pady=10)

number_text = StringVar()
number_label = Label(app, text='Total:', font=('bold', 10))
number_label.grid(row=4, column=0, sticky=W)
number_entry = Entry(app, textvariable=number_text, width=10)
number_entry.grid(row=4, column=1, padx=10, pady=10)

invoice_text = StringVar()
invoice_label = Label(app, text='Invoice Number:', font=('bold', 14))
invoice_label.grid(row=5, column=0, sticky=W)
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
comboBox.grid(row=5, column=1, padx=10, pady=10)
#clicked3 = StringVar(app, results_for_combobox)

get_btn = Button(app, text='Get Invoice', width=12, command=getrecord, font=('bold', 10))
get_btn.grid(row=6, column=0, padx=10, pady=10)

pay_btn = Button(app, text='Pay', width=12, command=payment, font=('bold', 10))
pay_btn.grid(row=7, column=0, padx=10, pady=10)

close_btn = Button(app, text='Close', width=12, command=quit, font=('bold', 10))
close_btn.grid(row=6, column=1, padx=10, pady=10)

app.title('Credit Card Payments')
app.geometry('300x350')

#start program
app.mainloop()

#https://stripe.com/docs/api/idempotent_requests
#https://stripe.com/docs/api/payment_methods/create