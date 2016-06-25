import MySQLdb
from Tkinter import *

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="root",  # your username
                     passwd="ali",  # your password
                     db="chcs")  # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM YOUR_TABLE_NAME")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

db.close()

window = Tk()
window.title("Health Care System")
window.resizable(width=False, height=False)
window.geometry('{}x{}'.format(500, 300))


# def ok_button_config():
#     x = queryString.get()
#     if x:
#         okButton.config(state='normal')
#     else:
#         okButton.config(state='disabled')
#
#
# queryString = StringVar(window)
# queryString.trace("w", ok_button_config)fdsd

queryLabel = Label(window, text="Enter Query: ")
queryLabel.pack()

# queryEntry = Entry(window, width=50, textvariable=queryString)
queryEntry = Entry(window, width=50)
queryEntry.pack()
# queryEntry.pack(side = RIGHT)

okButton = Button(window, text="OK")
okButton.pack()
# okButton.pack(side = BOTTOM)

resultLabel = Label(window, text="Result: ")
resultLabel.pack()

window.mainloop()
