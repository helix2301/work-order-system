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
    cur.execute("select * from workorders where status != 'closed'")
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", tk.END, values=row)
    conn.close()


connect()  #  this to create the db

root = tk.Tk()
root.geometry("1975x300")
root.title('Work Order List')

tree= ttk.Treeview(root, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8", "column9","column10","column11"), show='headings')
tree.heading("#1", text="Status")
tree.heading("#2", text="Priority")
tree.heading("#3", text="Company Name")
tree.heading("#4", text="First Name")
tree.heading("#5", text="Last Name")
tree.heading("#6", text="Phone")
tree.heading("#7", text="E-Mail")
tree.heading("#8", text="Description")
tree.heading("#9", text="Work Order Number")
tree.heading("#10", text="Resolution")
tree.heading("#11", text="Tech")
tree.pack()

b2 = tk.Button(text="view data", command=View)
b2.pack()

root.mainloop()