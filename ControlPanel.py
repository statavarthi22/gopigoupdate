from tkinter import *
from tkinter import messagebox
import tkinter as tk

# import the time library for the sleep function
import time
# import the GoPiGo3 drivers
import easygopigo3 as easy

import urllib.request, json

import platform

##Sentinel Up Configurations
ver = "1.1"

pCode = "b0a440b5-9230-4365-998a-2eee6dbc303b"

os = platform.system()+"%20"+platform.release()

dId = "dex123"

apiKey="a54945822d049bd2b1c4cb798b13ae81"

arch = platform.machine()

upURL = "https://up.sentinelcloud.com/api?key="

url=upURL+apiKey+"&productCode="+pCode+"&productVersion="+ver+"&format=json&id="+dId+"&os="+os+"&arch="+arch+"&lang=en";

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
    
def applyPayLoad():
    ## Open a file
    fo = open("ControlPanel.py", "w")
    fo.write(getPayLoad(data))
    ## Close opened file
    fo.close()
    
    messagebox.showinfo("","Update Applied. Restart application")
        
def updatesAvailable(data):
    return len(data['updates'])


# Create an instance of the GoPiGo3 class.
# GPG will be the GoPiGo3 object.
gpg = easy.EasyGoPiGo3()

def forward():
    gpg.forward()
    
def stop():
    gpg.stop()
    
def left():
    gpg.left()
    time.sleep(1.2)
    gpg.forward()
    
def right():
    gpg.right()
    time.sleep(1.2)
    gpg.forward()
    
def back():
    gpg.backward()
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('1100x600')

def popup_bonus():
    win = tk.Toplevel()
    win.wm_title("Window")
    win.geometry('450x300')
    
    printText = "No updates available at this time"
    
    lblInvisible10 = Label(win, text="Updates   ", width="30", height="2", justify=CENTER)
    lblInvisible10.grid(row=0, columnspan=2)
    lblInvisible10.config(font=('calibri', 15, 'bold'))
    
    if updatesAvailable(data) > 0:
        
        updateVer = data['updates']['update'][0]['target']['version']
        
        updateDesc = data['updates']['update'][0]['title']
    
        printText = "Version "+updateVer+" is now available!"
    
        lblInvisible11 = Label(win, text=printText, height="5", justify=LEFT, wraplength=500)
        lblInvisible11.grid(row=1, columnspan=2)
        lblInvisible11.config(font=('calibri', 10, ''))

        lblInvisible12 = Label(win, text=updateDesc+" *", height="5", justify=LEFT, wraplength=500)
        lblInvisible12.grid(row=2, columnspan=2)
        lblInvisible12.config(font=('calibri', 10, ''))
    

        b = tk.Button(win, text="Apply", bg="Green", fg="white", width="15", command=applyPayLoad)
        b.grid(row=3, column=0)

        b2 = tk.Button(win, text="Ignore", command=win.destroy, bg="Green", fg="white", width="15")
        b2.grid(row=3, column=1)
        b2.focus()
    
        lblInvisible13 = Label(win, text="* Restart Required.", height="5", justify=LEFT, wraplength=500)
        lblInvisible13.grid(row=4, columnspan=2)
        lblInvisible13.config(font=('calibri', 10, ''))
        
    if updatesAvailable(data) == 0:
        
        lblInvisible14 = Label(win, text=printText, height="5", justify=LEFT, wraplength=500)
        lblInvisible14.grid(row=1, columnspan=2)
        lblInvisible14.config(font=('calibri', 10, ''))


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

btnFwd = Button(window, text="Forward", bg="Green", fg="white", width="10", command=forward)
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

btnLeft = Button(window, text="Left", bg="Green", fg="white", width="10", command=left)
btnLeft.config(font=('calibri', 20, 'bold'))
btnLeft.grid(column=0, row=3)

btnStop = Button(window, text="Stop", bg="red", fg="white", width="10", command=stop)
btnStop.config(font=('calibri', 20, 'bold'))
btnStop.grid(column=1, row=3)

btnRight = Button(window, text="Right", bg="Green", fg="white", width="10",command=right)
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

btnBack = Button(window, text="Back", bg="Green", fg="white", width="10", command=back)
btnBack.config(font=('calibri', 20, 'bold'))
btnBack.grid(column=1, row=5)

lblInvisible1 = Label(window, text="", width="35", height="5")
lblInvisible1.grid(column=2, row=5)
#

# Row 6

lblInvisible2 = Label(window, text="Software Version: " + ver, width="35", height="5")
lblInvisible2.grid(column=0, row=6)

lblInvisible1 = Label(window, text="", width="35", height="5")
lblInvisible1.grid(column=1, row=6)

btnUpdate = Button(window, text="Check for Updates", bg="Green", fg="white", width="15", command=popup_bonus)
btnUpdate.config(font=('calibri', 10, 'bold'))
btnUpdate.grid(column=2, row=6)



 
window.mainloop()