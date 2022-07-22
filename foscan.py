# ========================= code starts here ====================================
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import string

window = Tk()
window.geometry("400x380")
window.resizable(False, False)
window.title("GP Front Office Scanner")
himage = PhotoImage(file='./a.png')
Label(window, text="LB Front Office Scan", image=himage).grid(row=0, columnspan=2)


# program Functions
def newclicked():
    txtName.delete(0, END)


def ScanNow():
    print("Scan Request received")
    tempvar = scanner.get()
    varName=  txtName.get()
    varName=varName.replace (" ","_")
    varDocType=cmbDoctype.get()
    varDocType=varDocType.replace(" ","_")
    varFileName=varName+" "+varDocType+".pdf"
    print (varFileName)
    print(tempvar)
    if tempvar == 1:
        print("Normal Scan")
    elif tempvar == 2:
        print("Colour Scan")
    else:
        messagebox.showerror("Warning", "Please select Scan Type")



def about():
    messagebox.showinfo("GP Front Office Scanner", "Created by Arun Haridas \nTechnical Assistant\nMarangattupilly Gramapanchayat")

# Widgets
lblName = Label(window,
                text="Name of applicant",
                justify=LEFT)
txtName = Entry(window)
lblDocType = Label(window,
                   text="Document type")
cmbDoctype = ttk.Combobox(window,
                          values=["Application Form",
                                  "Ration Card",
                                  "Identity Card",
                                  "Building Plan"])
scanner = IntVar()
radiobwscan = ttk.Radiobutton(window,
                              text="Normal scan",
                              variable=scanner,
                              value=1)
radiocscan = ttk.Radiobutton(window,
                             text="Color scan",
                             variable=scanner,
                             value=2)
btnNew = ttk.Button(window,
                    text="New Application",
                    command=newclicked,
                    state=DISABLED)
btnScan = ttk.Button(window,
                     text="Scan",
                     command=ScanNow,
                     width=24)
btnDeleteOldScanned=ttk.Button(window,
                               text="Remove Old Scanned",
                               state=DISABLED,
                               width=20)
btnOpenScannedFolder=ttk.Button(window,
                                text="Open Scanned Folder",
                                state=DISABLED,
                                width=20)
btnOpenILGMS=ttk.Button(window,
                        text="Open ILGMS",
                        width=20,
                        state=DISABLED)
btnOpenMFSearch=ttk.Button(window,
                           text="Minor Function Search",
                           width=20,
                           state=DISABLED)
btnAbout=ttk.Button(window,
                    text="About",
                    width=20,
                    command=about)
btnSettings=ttk.Button(window,
                   text="Settings",
                   width=20,
                   state=DISABLED)


# UI
lblName.grid(row=1, column=0, sticky=W)
txtName.grid(row=1, column=1, sticky=W)
lblDocType.grid(row=2, column=0, sticky=W)
cmbDoctype.grid(row=2, column=1, sticky=W)
radiobwscan.grid(row=3, column=1, sticky=W)
scanner.set(1)
radiocscan.grid(row=4, column=1, sticky=W)
btnNew.grid(row=5, column=0)
btnScan.grid(row=5, column=1, sticky=W)
Label(window, text=" ").grid(row=6)
btnDeleteOldScanned.grid(row=7, column=0)
btnOpenScannedFolder.grid(row=7, column=1)
btnOpenILGMS.grid(row=8, column=0)
btnOpenMFSearch.grid(row=8, column=1)
Label(window, text=" ").grid(row=9)
btnAbout.grid(row=10,column=0)
btnSettings.grid(row=10, column=1)


window.mainloop()