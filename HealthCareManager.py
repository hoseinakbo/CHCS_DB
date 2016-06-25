import MySQLdb
from Tkinter import *


def setup_table(query):
    cur.execute(query)
    print(cur.fetchall())
    table(cur.fetchall)


def okOnClick():
   print(queryEntry.get())
   setup_table(queryEntry.get())



def gui_setup():
    window = Tk()
    window.title("Health Care System")
    window.resizable(width=False, height=False)
    window.geometry('{}x{}'.format(500, 300))

    queryLabel = Label(window, text="Enter Query: ")
    queryLabel.pack()

    global queryEntry
    queryEntry = Entry(window, width=50)
    queryEntry.pack()

    okButton = Button(window, text="OK", command=okOnClick)
    okButton.pack()

    resultLabel = Label(window, text="Result: ")
    resultLabel.pack()

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



def table(data):
    global rows
    rows = []
    for i in range(len(data)):
        cols = []
        for j in range(len(data[0])):
            e = Entry(relief=RIDGE)
            e.grid(row=i, column=j, sticky=NSEW)
            e.insert(END, data[i][j])
            cols.append(e)
        rows.append(cols)

def onPress():
    for row in rows:
        for col in row:
            print col.get(),
        print



# db.close()


