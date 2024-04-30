from tkinter import ttk
import tkinter as tk
import sqlite3
import os


def connect():
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    conn.commit()
    conn.close()


def View():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR + '\\store.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM invoices")
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", tk.END, values=row)
    conn.close()


connect()  #  this to create the db

root = tk.Tk()
root.geometry("2200x300")
root.title('All Invoices')

tree= ttk.Treeview(root, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8", "column9","column10","column11"), show='headings')
tree.heading("#1", text="Company Name")
tree.heading("#2", text="Today's Date")
tree.heading("#3", text="Invoice Number")
tree.heading("#4", text="Due Date")
tree.heading("#5", text="Part Description")
tree.heading("#6", text="Part Price")
tree.heading("#7", text="Labor Price")
tree.heading("#8", text="Description")
tree.heading("#9", text="Sales Tax")
tree.heading("#10", text="Total")
tree.heading("#11", text="Paid")
tree.pack()

b2 = tk.Button(text="view data", command=View)
b2.pack()

root.mainloop()