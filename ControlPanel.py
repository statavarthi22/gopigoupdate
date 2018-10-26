from tkinter import *
from tkinter import messagebox
import tkinter as tk

# import the time library for the sleep function
import time
# import the GoPiGo3 drivers
#import easygopigo3 as easy

import urllib.request, json

url="https://up.sentinelcloud.com/api?key=a54945822d049bd2b1c4cb798b13ae81&productCode=b0a440b5-9230-4365-998a-2eee6dbc303b&productVersion=1.0&format=json&id=dex123&os=Linux&arch=x86&lang=en";

response = urllib.request.urlopen(url)

data = json.loads(response.read().decode('utf8'))

def getPayLoad(data):
    #Check for updates:

    print(len(data['updates']))

    if len(data['updates']) > 0:

        updateURL = data['updates']['update'][0]['file']

        updateAction = urllib.request.urlopen(updateURL)

        updateCode=updateAction.read().decode('utf8')
        
        return updateCode
    
    if len(data['updates']) == 0:
        return "NONE"
    
def applyPayLoad(data):
    ## Open a file
    fo = open("update.py", "w")
    fo.write(getPayLoad(data))
    ## Close opened file
    fo.close()
    
applyPayLoad(data)


#
#import update


 
window = Tk()
 
window.title("Welcome to GoPiGo")
 
window.geometry('1750x1200')

    
def popup_bonus():
    win = tk.Toplevel()
    win.wm_title("Window")
    win.geometry('650x650')

    lblInvisible10 = Label(win, text="Updates   ", width="30", height="2", justify=CENTER)
    lblInvisible10.grid(row=0, columnspan=2)
    lblInvisible10.config(font=('calibri', 15, 'bold'))
    
    lblInvisible11 = Label(win, text="Version 1.1 Avilable!", height="5", justify=LEFT, wraplength=500)
    lblInvisible11.grid(row=1, columnspan=2)
    lblInvisible11.config(font=('calibri', 10, ''))

    lblInvisible12 = Label(win, text="Can detect navigate around obstacles *", height="5", justify=LEFT, wraplength=500)
    lblInvisible12.grid(row=2, columnspan=2)
    lblInvisible12.config(font=('calibri', 10, ''))
    

    b = tk.Button(win, text="Apply", command=win.destroy, bg="Green", fg="white", width="15")
    b.grid(row=3, column=0)

    b = tk.Button(win, text="Ignore", command=win.destroy, bg="Green", fg="white", width="15")
    b.grid(row=3, column=1)
    
    lblInvisible11 = Label(win, text="* Restart Required.", height="5", justify=LEFT, wraplength=500)
    lblInvisible11.grid(row=4, columnspan=2)
    lblInvisible11.config(font=('calibri', 10, ''))

#window.columnconfigure(0, pad=3)
#window.columnconfigure(1, pad=3)
#window.columnconfigure(2, pad=3)
#        
#window.rowconfigure(0, pad=3)
#window.rowconfigure(1, pad=3)
#window.rowconfigure(2, pad=3)
#window.rowconfigure(3, pad=3)
#window.rowconfigure(4, pad=3)


 
#lbl = Label(window, text="Hello")
 
#lbl.grid(column=0, row=0)

#def clicked():
 
    #lbl.configure(text="Button was clicked !!")
 
#btn = Button(window, text="Click Me", bg="red", fg="white", command=clicked)

#Row 0

lblInvisible1 = Label(window, text="", width="20", height="5")
lblInvisible1.grid(column=0, row=0)

lblInvisible1 = Label(window, text="GoPiGo Control Panel", width="35", height="5")
lblInvisible1.grid(column=1, row=0)
lblInvisible1.config(font=('calibri', 10, 'bold'))


lblInvisible1 = Label(window, text="", width="20", height="5")
lblInvisible1.grid(column=2, row=0)

#Row 1

lblInvisible1 = Label(window, text="", width="35", height="5")
lblInvisible1.grid(column=0, row=1)

btnFwd = Button(window, text="Forward", bg="Green", fg="white", width="10")
btnFwd.config(font=('calibri', 20, 'bold'))
btnFwd.grid(column=1, row=1)

lblInvisible1 = Label(window, text="", width="35", height="5")
lblInvisible1.grid(column=2, row=1)

#Row 2

lblInvisible1 = Label(window, text="", width="50", height="5")
lblInvisible1.grid(column=0, row=2)

lblInvisible1 = Label(window, text="", width="35", height="5")
lblInvisible1.grid(column=1, row=2)

lblInvisible1 = Label(window, text="", width="35", height="5")
lblInvisible1.grid(column=2, row=2)

#Row 3

btnLeft = Button(window, text="Left", bg="Green", fg="white", width="10")
btnLeft.config(font=('calibri', 20, 'bold'))
btnLeft.grid(column=0, row=3)

btnStop = Button(window, text="Stop", bg="red", fg="white", width="10")
btnStop.config(font=('calibri', 20, 'bold'))
btnStop.grid(column=1, row=3)

btnRight = Button(window, text="Right", bg="Green", fg="white", width="10")
btnRight.config(font=('calibri', 20, 'bold'))
btnRight.grid(column=2, row=3)

#Row 4

lblInvisible1 = Label(window, text="", width="50", height="5")
lblInvisible1.grid(column=0, row=4)

lblInvisible1 = Label(window, text="", width="35", height="5")
lblInvisible1.grid(column=1, row=4)

lblInvisible1 = Label(window, text="", width="35", height="5")
lblInvisible1.grid(column=2, row=4)

#Row 5

lblInvisible1 = Label(window, text="", width="35", height="5")
lblInvisible1.grid(column=0, row=5)

btnBack = Button(window, text="Back", bg="Green", fg="white", width="10")
btnBack.config(font=('calibri', 20, 'bold'))
btnBack.grid(column=1, row=5)

lblInvisible1 = Label(window, text="", width="35", height="5")
lblInvisible1.grid(column=2, row=5)
#

# Row 6

lblInvisible2 = Label(window, text="Software Version: 1.0", width="35", height="5")
lblInvisible2.grid(column=0, row=6)

lblInvisible1 = Label(window, text="", width="35", height="5")
lblInvisible1.grid(column=1, row=6)

btnUpdate = Button(window, text="Check for Updates", bg="Green", fg="white", width="15", command=popup_bonus)
btnUpdate.config(font=('calibri', 10, 'bold'))
btnUpdate.grid(column=2, row=6)

 
window.mainloop()

