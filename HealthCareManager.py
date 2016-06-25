import ttk

import MySQLdb
from Tkinter import *


def show_table():
    rows = []
    i = 0
    for data_row in cur.fetchall():
        cols = []
        j = 0
        for data_col in data_row:
            e = Entry(window, relief=RIDGE)
            e.grid(row=i, column=j, sticky=NSEW)
            e.insert(END, data_col)
            cols.append(e)
            j += 1
        rows.append(cols)
        i += 1


def okOnClick():
    print(queryEntry.get())
    cur.execute(queryEntry.get())
    show_table()


def gui_setup():
    global window
    # window = Tk()
    # window.title("Health Care System")
    # window.geometry('{}x{}'.format(500, 300))
    #
    # queryLabel = Label(window, text="Enter Query: ")
    # queryLabel.pack()
    #
    # global queryEntry
    # queryEntry = Entry(window, width=50)
    # queryEntry.pack()
    #
    # okButton = Button(window, text="OK", command=okOnClick)
    # okButton.pack()
    #
    # resultLabel = Label(window, text="Result: ")
    # resultLabel.pack()

    window = ttk.Panedwindow(parent, orient=VERTICAL)
    # first pane, which would get widgets gridded into it:
    f1 = ttk.Labelframe(p, text='Pane1', width=100, height=100)
    f2 = ttk.Labelframe(p, text='Pane2', width=100, height=100)  # second pane
    p.add(f1)
    p.add(f2)

    # resultsLabel = Text(window, height=5, width=30)
    # resultsLabel.pack()

    window.mainloop()


db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="root",  # your username
                     passwd="95649",  # your password
                     db="chcs")  # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
# cur.execute("SELECT * FROM Patient;")

# print all the first cell of all the rows
# for row in cur.fetchall():
#     print row
gui_setup()


# db.close()
