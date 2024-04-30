from tkinter import *
#from databases import Database
import sys
import sqlite3
import os
#import subprocess
from tkinter import ttk
#from tkinter import messagebox
from datetime import date
from tkinter import messagebox
from tkinter import ttk

### get PDF file libraries  
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import  A4

#create window

app = Tk()

CN_text = StringVar()
CN_label = Label(app, text='Company Name:', font=('bold', 14))
CN_label.grid(row=0, column=0, sticky=W)
CN_entry = Entry(app, textvariable=CN_text, width=30)

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
comboBox.grid(row=0, column=1, padx=10, pady=10)
clicked3 = StringVar(app, results_for_combobox)

invoice_text = StringVar()
invoice_label = Label(app, text='Invoice Number:', font=('bold', 14))
invoice_label.grid(row=2, column=0, sticky=W)
invoice_entry = Entry(app, textvariable=invoice_text, width=10)
invoice_entry.grid(row=2, column=1, padx=10, pady=10)

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
des_label.grid(row=7, column=0, sticky=W)
des_entry = Entry(app, textvariable=des_text, width=50)
des_entry.grid(row=7, column=1, padx=10, pady=10)

tax_text = StringVar()
tax_label = Label(app, text='Tax:', font=('bold', 14))
tax_label.grid(row=8, column=0, sticky=W)
tax_entry = Entry(app, textvariable=tax_text, width=10)
tax_entry.grid(row=8, column=1, padx=10, pady=10)

total_text = StringVar()
total_label = Label(app, text='Total:', font=('bold', 14))
total_label.grid(row=9, column=0, sticky=W)
total_entry = Entry(app, textvariable=total_text, width=10)
total_entry.grid(row=9, column=1, padx=10, pady=10)

def print():
    CN = clicked3.get()
    invoice = invoice_text.get()
    cal2 = cal2_text.get()
    parts = parts_text.get()
    parts_price = parts_price_text.get()
    labor = labor_text.get()
    des = des_text.get()
    tax = tax_text.get()
    total = total_text.get()
    today = date.today()
    #create PDF file
    pdf_name = ("Invoice Number" + str(invoice) + ".pdf")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    save_name = os.path.join(BASE_DIR, "invoices", pdf_name)
    c = canvas.Canvas(save_name, pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(30,750,"Customer Name: " + CN)
    c.drawString(30,710,"Invoice# " + invoice)
    c.drawString(30,690,"Date: " + str(today))
    c.drawString(30,670,"Due Date: " + cal2)
    c.drawString(30,650,"Part Description: " + parts)
    c.drawString(30,630,"Part Price: " + parts_price)
    c.drawString(30,610,"Labor: " + labor)
    c.drawString(30,590,"Description: " + des)
    c.drawString(30,570,"Tax: " + tax)
    c.drawString(30,550,"Total: " + total)
    c.showPage()
    c.save()
    os.startfile(os.path.join(BASE_DIR, "invoices", pdf_name))

def save():
    if invoice_text.get():
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR + '\\store.db')
        my_conn = sqlite3.connect(db_path)
        CN = comboBox.get()
        today = date.today()
        invoice = invoice_text.get()
        cal2 = cal2_text.get()
        parts = parts_text.get()
        parts_price = parts_price_text.get()
        labor = labor_text.get()
        des = des_text.get()
        tax = tax_text.get()
        total = total_text.get()
        my_data=(CN, today, invoice, cal2, parts, parts_price, labor, des, tax, total)
        my_query="INSERT INTO invoices VALUES (?,?,?,?,?,?,?,?,?,?,null)"
        my_conn.execute(my_query,my_data)
        my_conn.commit()
        messagebox.showinfo("About",  "Your invoice has been saved!")
    else:
        messagebox.showerror('Error', 'Please enter all information')

def new():
    #clear the text boxes
    parts_entry.delete(0, END)
    parts_price_entry.delete(0, END)
    labor_entry.delete(0, END)
    des_entry.delete(0, END)
    tax_entry.delete(0, END)
    total_entry.delete(0, END)
    invoice_entry.delete(0, END)

def quit():
    sys.exit()

add_btn = Button(app, text='New Invoice', width=12, command=new)
add_btn.grid(row=11, column=0, padx=10, pady=10)

save_btn = Button(app, text='Save', width=12, command=save)
save_btn.grid(row=12, column=0, padx=10, pady=10)

cl_btn = Button(app, text='Print', width=12, command=print)
cl_btn.grid(row=11, column=1, padx=10, pady=10)

close_btn = Button(app, text='Close', width=12, command=quit)
close_btn.grid(row=12, column=1, padx=10, pady=10)

app.title('Invoice Generator')
app.geometry('500x485')

#start program
app.mainloop()

#https://www.plus2net.com/python/tkinter-DateEntry.php
