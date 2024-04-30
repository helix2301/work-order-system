from tkinter import *
from databases import Database
import sys
import sqlite3
import os
from tkinter import ttk
from tkinter import messagebox

my_conn = sqlite3.connect('store.db')

def add():
    ST = ST_text.get()
    PR = PR_text.get()
    CN = CN_text.get()
    FN = FN_text.get()
    LN = LN_text.get()
    des = des_text.get()
    email = email_text.get()
    phone = phone_text.get()
    my_data=(ST, PR, CN, FN, LN, phone, email, des)
    my_query="INSERT INTO workorders VALUES (?,?,?,?,?,?,?,?)"
    my_conn.execute(my_query,my_data)
    my_conn.commit()
    ST_entry.delete(0, 255)
    PR_entry.delete(0, 255)
    CN_entry.delete(0, 255)
    FN_entry.delete(0, 255)
    LN_entry.delete(0, 255)
    phone_entry.delete(0, 255)
    email_entry.delete(0, 255)
    des_entry.delete(0, 255)

#create window

app = Tk()

ST_text = StringVar()
ST_label = Label(app, text='Status:', font=('bold', 14))
ST_label.grid(row=0, column=0, sticky=W)
ST_entry = Entry(app, textvariable=ST_text, width=30)
ST_entry.grid(row=0, column=1, padx=10, pady=10)

PR_text = StringVar()
PR_label = Label(app, text='Priority:', font=('bold', 14))
PR_label.grid(row=1, column=0, sticky=W)
PR_entry = Entry(app, textvariable=PR_text, width=30)
PR_entry.grid(row=1, column=1, padx=10, pady=10)

CN_text = StringVar()
CN_label = Label(app, text='Company Name:', font=('bold', 14))
CN_label.grid(row=2, column=0, sticky=W)
CN_entry = Entry(app, textvariable=CN_text, width=30)
CN_entry.grid(row=2, column=1, padx=10, pady=10)

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
phone_label = Label(app, text='Phone:', font=('bold', 14))
phone_label.grid(row=5, column=0, sticky=W)
phone_entry = Entry(app, textvariable=phone_text, width=30)
phone_entry.grid(row=5, column=1, padx=10, pady=10)

email_text = StringVar()
email_label = Label(app, text='email:', font=('bold', 14))
email_label.grid(row=6, column=0, sticky=W)
email_entry = Entry(app, textvariable=email_text, width=30)
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

wo_text = StringVar()
wo_label = Label(app, text='work order#:', font=('bold', 14))
wo_label.grid(row=9, column=0, sticky=W)
wo_entry = Entry(app, textvariable=wo_text, width=20)
wo_entry.grid(row=9, column=1, padx=10, pady=10)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR + '\\store.db')
my_conn = sqlite3.connect(db_path)
curs = my_conn.cursor()
curs.execute("select WordOrdernum from workorders where status != 'closed'")
results = curs.fetchall()
curs.close()
my_conn.close()
results_for_combobox = [result[0] for result in results]
comboBox = ttk.Combobox(app,values=results_for_combobox)
comboBox.grid(row=9, column=1, padx=10, pady=10)
clicked3 = StringVar(app, results_for_combobox)

tech_text = StringVar()
tech_label = Label(app, text='Tech:', font=('bold', 14))
tech_label.grid(row=10, column=0, sticky=W)
tech_entry = Entry(app, textvariable=res_text, width=20)
tech_entry.grid(row=10, column=1, padx=10, pady=10)

def getrecord():
    ST_entry.delete(0, 255)
    PR_entry.delete(0, 255)
    CN_entry.delete(0, 255)
    FN_entry.delete(0, 255)
    LN_entry.delete(0, 255)
    phone_entry.delete(0, 255)
    email_entry.delete(0, 255)
    des_entry.delete(0, 255)
    tech_entry.delete(0, 255)
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
        tech_entry.insert(END, record[8])

def closerecord():
    if res_entry.get():
        SET = "closed"
        record_id = comboBox.get()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR + '\\store.db')
        my_conn = sqlite3.connect(db_path)
        cursor = my_conn.cursor()
        cursor.execute(f"UPDATE workorders SET status='{SET}', Resolution='{res_entry.get()}' where WordOrdernum = " + record_id)
        my_conn.commit()
        sys.exit()
    else:
        messagebox.showerror('Error', 'Please enter resolution')

add_btn = Button(app, text='Get Work Order', width=12, command=getrecord)
add_btn.grid(row=11, column=0, padx=10, pady=10)

cl_btn = Button(app, text='Close Order', width=12, command=closerecord)
cl_btn.grid(row=11, column=1, padx=10, pady=10)

app.title('Close Work Order')
app.geometry('470x500')

#start program
app.mainloop()
