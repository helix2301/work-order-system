from tkinter import ttk
import tkinter as tk
import sqlite3
import os


root = tk.Tk()
root.geometry("2200x400")
root.title('Customer List')

#def connect():
 #   conn = sqlite3.connect("store.db")
 #   cur = conn.cursor()
 #   conn.commit()
 #   conn.close()

def View():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR + '\\store.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(""" SELECT * FROM customers """)
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", tk.END, values=row)
    conn.close()

#connect()  #  this to create the db

tree= ttk.Treeview(root, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8", "column9", "column10", "column11"), show='headings')
tree.heading("#1", text="CUSTOMER NUMBER")
tree.heading("#2", text="FIRST NAME")
tree.heading("#3", text="LAST NAME")
tree.heading("#4", text="COMPANY NAME")
tree.heading("#5", text="EMAIL")
tree.heading("#6", text="PHONE")
tree.heading("#7", text="ADDRESS")
tree.heading("#8", text="CITY")
tree.heading("#9", text="STATE")
tree.heading("#10", text="ZIP")
tree.heading("#11", text="COUNTRY")
tree.pack()

b2 = tk.Button(text="view data", command=View)
b2.pack()

root.mainloop()