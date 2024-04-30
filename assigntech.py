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
curs.execute("select WordOrdernum from workorders where tech is null")
results = curs.fetchall()
curs.close()
my_conn.close()
results_for_combobox = [result[0] for result in results]
comboBox1 = ttk.Combobox(app,values=results_for_combobox)
comboBox1.grid(row=1, column=1, padx=10, pady=10)
#clicked3 = StringVar(app, results_for_combobox)

CN_text = StringVar()
CN_label = Label(app, text='Tech:', font=('bold', 14))
CN_label.grid(row=2, column=0, sticky=W)
CN_entry = Entry(app, textvariable=CN_text, width=30)
#CN_entry.grid(row=2, column=1, padx=10, pady=10)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR + '\\store.db')
my_conn = sqlite3.connect(db_path)
curs = my_conn.cursor()
curs.execute('select "First Name" from techs;')
results = curs.fetchall()
curs.close()
my_conn.close()
results_for_combobox = [result[0] for result in results]
comboBox2 = ttk.Combobox(app,values=results_for_combobox)
comboBox2.grid(row=2, column=1, padx=10, pady=10)
#clicked3 = StringVar(app, results_for_combobox)

def quit():
    sys.exit()

def closerecord():
    tech = comboBox2.get()
    record_id = comboBox1.get()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR + '\\store.db')
    my_conn = sqlite3.connect(db_path)
    cursor = my_conn.cursor()
    cursor.execute(f"UPDATE workorders SET tech='{tech}'where WordOrdernum = " + record_id)
    my_conn.commit()
    sys.exit()

add_btn = Button(app, text='Assign Tech', width=12, command=closerecord)
add_btn.grid(row=12, column=0, padx=10, pady=10)

close_btn = Button(app, text='Close', width=12, command=quit)
close_btn.grid(row=12, column=1, padx=10, pady=10)

app.title('Assign Tech')
app.geometry('325x125')

#start program
app.mainloop()

#https://www.plus2net.com/python/tkinter-DateEntry.php