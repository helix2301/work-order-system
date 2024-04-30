import os
from subprocess import call
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import csv

def about():
    messagebox.showinfo('About', 'SBS System\nVersion 1.1\n\nCreated by: Lipani Technologies LLC\n\nContact: 1-570-815-3774\n\nEmail: brandon@technologies.com\n\nWebsite: https://lipanitech.com')

def addcus():
    file = r'addcustomer.exe'
    os.startfile(os.path.normpath(file))

def allcus():
    file = r'customerlist.exe'
    os.startfile(os.path.normpath(file))

def newwo():
    file = r'createworkorder.exe'
    os.startfile(os.path.normpath(file))

def closewo():
    file = r'editworkorder.exe'
    os.startfile(os.path.normpath(file))

def allwo():
    file = r'allworkorders.exe'
    os.startfile(os.path.normpath(file))

def print():
    file = r'printworkorders.exe'
    os.startfile(os.path.normpath(file))

def maps():
    file = r'maps.exe'
    os.startfile(os.path.normpath(file))

def createIV():
    file = r'invoicing.exe'
    os.startfile(os.path.normpath(file))

def closeIV():
    file = r'closeinvoice.exe'
    os.startfile(os.path.normpath(file))

def AllIV():
    file = r'allinvoices.exe'
    os.startfile(os.path.normpath(file))

def quit():
    sys.exit()

def exportinvoices():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR + '\\store.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("select * from invoices")
    with open("invoice_data.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow([i[0] for i in cur.description])
        csv_writer.writerows(cur)
    messagebox.showinfo('Success', 'Invoices exported to invoice_data.csv')
    conn.close()

def exportworkorders():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR + '\\store.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("select * from workorders")
    with open("workorder_data.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow([i[0] for i in cur.description])
        csv_writer.writerows(cur)
    messagebox.showinfo('Success', 'Work Orders exported to workorder_data.csv')
    conn.close()

def exportcustomers():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR + '\\store.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("select * from customers")
    with open("customer_data.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow([i[0] for i in cur.description])
        csv_writer.writerows(cur)
    messagebox.showinfo('Success', 'Customers exported to customer_data.csv')
    conn.close()

def openinvoice():
    file = r'invoice_data.csv'
    os.startfile(os.path.normpath(file))

def openworkorders():
    file = r'workorder_data.csv'
    os.startfile(os.path.normpath(file))

def opencustomerdata():
    file = r'customer_data.csv'
    os.startfile(os.path.normpath(file))

app = Tk()

cust_label = Label(app, text='Customers', font=('bold', 14))
cust_label.grid(row=0, column=0, sticky=W)

add_btn = Button(app, text='Add Customer', width=12, command=addcus)
add_btn.grid(row=2, column=0, padx=10, pady=10)

allcus_btn = Button(app, text='All Customers', width=12, command=allcus)
allcus_btn.grid(row=2, column=1, padx=10, pady=10)

cust_label = Label(app, text='Work Orders', font=('bold', 14))
cust_label.grid(row=3, column=0, sticky=W)

newWO_btn = Button(app, text='New Work Order', width=15, command=newwo)
newWO_btn.grid(row=5, column=0, padx=10, pady=10)

closeWO_btn = Button(app, text='Close Work Order', width=15, command=closewo)
closeWO_btn.grid(row=5, column=1, padx=10, pady=10)

All_WO_btn = Button(app, text='All Work Orders', width=12, command=allwo)
All_WO_btn.grid(row=5, column=2, padx=10, pady=10)

print_btn = Button(app, text='Print Work Order', width=15, command=print)
print_btn.grid(row=5, column=3, padx=10, pady=10)

maps_btn = Button(app, text='Maps', width=15, command=maps)
maps_btn.grid(row=5, column=4, padx=10, pady=10)

cust_label = Label(app, text='Invoicing', font=('bold', 14))
cust_label.grid(row=6, column=0, sticky=W)

createIV_btn = Button(app, text='Create Invoice', width=15, command=createIV)
createIV_btn.grid(row=7, column=0, padx=10, pady=10)

CloseIV_btn = Button(app, text='Close Invoice', width=15, command=closeIV)
CloseIV_btn.grid(row=7, column=1, padx=10, pady=10)

AllIV_btn = Button(app, text='All Invoices', width=15, command=AllIV)
AllIV_btn.grid(row=7, column=2, padx=10, pady=10)

cust_label = Label(app, text='Techs', font=('bold', 14))
cust_label.grid(row=8, column=0, sticky=W)

add_tech = Button(app, text='Add Tech', width=12, command=addcus)
add_tech.grid(row=9, column=0, padx=10, pady=10)

assign_tech = Button(app, text='Assign Tech', width=12, command=addcus)
assign_tech.grid(row=9, column=1, padx=10, pady=10)

OWO_tech = Button(app, text='Open Work Orders', width=15, command=addcus)
OWO_tech.grid(row=9, column=2, padx=10, pady=10)

cust_label = Label(app, text='Calendar', font=('bold', 14))
cust_label.grid(row=10, column=0, sticky=W)

add_tech = Button(app, text='Scheduling Calendar', width=15, command=addcus)
add_tech.grid(row=11, column=0, padx=10, pady=10)

#menu Bar
menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)

exportsmenu = Menu(menubar, tearoff=0)
exportsmenu.add_command(label="Export Invoices", command=exportinvoices)
exportsmenu.add_command(label="Export Work Orders", command=exportworkorders)
exportsmenu.add_command(label="Export Customers", command=exportcustomers)
exportsmenu.add_separator()
exportsmenu.add_command(label="Open Invoices Export", command=openinvoice)
exportsmenu.add_command(label="Open Work Orders Export", command=openworkorders)
exportsmenu.add_command(label="Open Customers Export", command=opencustomerdata)
menubar.add_cascade(label="Exports", menu=exportsmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

app.title('Lipani Tech SBS')
app.geometry('700x450')

#write table to csv

#start program
app.config(menu=menubar)
app.mainloop()

#Features Added 1.1
#Added Print Work Order
#Added About Menu
#Added Exit Menu
#comboboxes
#invoice system
#maps

#https://gist.github.com/shitalmule04/82d2091e2f43cb63029500b56ab7a8cc
#https://gist.github.com/shitalmule04/82d2091e2f43cb63029500b56ab7a8cc
#https://www.youtube.com/watch?v=_dKVTqWwN4U&t=4s