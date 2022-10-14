"""
    Front Office Scanner application for Gramapanchayat ILGMS
    Copyright (C) 2022  Arun Haridas

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import string
import os
import webbrowser

AppVersion="0.2 (Alpha edition)"
window = Tk()
window.geometry("400x380")
window.resizable(False, False)
window.title("GP Front Office Scanner")
himage = PhotoImage(file="./a.png")
Label(window, text="LB Front Office Scan", image=himage).grid(row=0, columnspan=2)


# program Functions
def newclicked():
    txtName.delete(0, END)

def setproperfilename(fname):                           # file name correct
    fname = fname.replace(" ","_")
    fname = fname.replace("/","-")
    fname = fname.replace("/", "-")
    fname = fname.replace("?", "-")
    fname = fname.replace(";", "-")
    fname = fname.replace(":", "-")
    fname = fname.replace("<", "-")
    fname = fname.replace(">", "-")
    return fname

def ScanNow():                                                                                                          #Main Scan Function
    print("Scan Request received")
    tempvar: int = scanner.get()
    varName = txtName.get()
    varName = setproperfilename(varName)
    varDocType=cmbDoctype.get()
    varDocType=setproperfilename(varDocType)
    varFileName=varName+" "+varDocType+".pdf"
    print (varFileName)
    print(tempvar)
    if (varName=="") or (varDocType==""):
        messagebox.showerror("Error", "Please check application name and Document type")
    else:
        if tempvar == 1:                                # Normal Scan
            cmd='NAPS2.Console.exe -o "Scanned\\' + varFileName +'" --progress'
            os.system(cmd)
        elif tempvar == 2:                              # Text Scan
            cmd='NAPS2.Console.exe -o "Scanned\\' + varFileName +'" --progress --profile ilgms-t'
            os.system(cmd)  
        elif tempvar==3:                                # Color Scan
            cmd='NAPS2.Console.exe -o "Scanned\\' + varFileName +'" --progress --profile ilgms-c'
            os.system(cmd)  
        else:
            messagebox.showerror("Warning", "Please select Scan Type")

def openscanned():
    cmd='explorer scanned\\'
    os.system(cmd)  

def clearscanned():
    cmd='copy????'
    os.system(cmd)  

def openilgms():
    webbrowser.open_new_tab("https://ilgms.lsgkerala.gov.in/")

def opengptools():
    webbrowser.open_new_tab("http://gptools.rancorfighters.com")

def opensite():
    webbrowser.open_new_tab("https://foscan.blogspot.com/")


def about():
    messagebox.showinfo("About", "GP Front Office Scanner\n"
                                 "Version : "+AppVersion+"\n\n"
                                 "Created by \n"
                                 "Arun Haridas \n"
                                 "Technical Assistant\n"
                                 "Marangattupilly Gramapanchayat")

# Widgets
lblName = Label(window,
                text="Name of applicant",
                justify=LEFT)
txtName = Entry(window)
lblDocType = Label(window,
                   text="Document type")
cmbDoctype = ttk.Combobox(window,
                          values=["Income Certificate",
                                  "Application Form",
                                  "Ration Card",
                                  "Identity Card",
                                  "Building Plan"])
scanner = IntVar()
radionscan = ttk.Radiobutton(window,
                              text="Normal scan",
                              variable=scanner,
                              value=1)
"""
radiotscan = ttk.Radiobutton(window,
                             text="Text scan",
                             variable=scanner,
                             value=2)
radiocscan = ttk.Radiobutton(window,
                             text="Color scan",
                             variable=scanner,
                             value=3)
"""
btnNew = ttk.Button(window,
                    text="New Application",
                    command=newclicked,)
btnScan = ttk.Button(window,
                     text="Scan",
                     command=ScanNow,
                     width=24)
btnDeleteOldScanned=ttk.Button(window,
                               text="Remove Old Scanned",
                               command=clearscanned,
                               width=20)
btnOpenScannedFolder=ttk.Button(window,
                                text="Open Scanned Folder",
                                command=openscanned,
                                width=20)
btnOpenILGMS=ttk.Button(window,
                        text="Open ILGMS",
                        width=20,
                        command=openilgms)
btnOpenMFSearch=ttk.Button(window,
                           text="GP Tools",
                           width=20,
                           command=opengptools)
btnAbout=ttk.Button(window,
                    text="About",
                    width=20,
                    command=about)
btnSettings=ttk.Button(window,
                   text="Help / Website",
                   width=20,
                   command=opensite)


# UI
lblName.grid(row=1, column=0, sticky=W)
txtName.grid(row=1, column=1, sticky=W)
lblDocType.grid(row=2, column=0, sticky=W)
cmbDoctype.grid(row=2, column=1, sticky=W)
radionscan.grid(row=3, column=1, sticky=W)
scanner.set(1)
#radiotscan.grid(row=4, column=1, sticky=W)
#radiocscan.grid(row=5, column=1, sticky=W)
btnNew.grid(row=6, column=0)
btnScan.grid(row=6, column=1, sticky=W)
Label(window, text=" ").grid(row=7)
btnDeleteOldScanned.grid(row=8, column=0)
btnOpenScannedFolder.grid(row=8, column=1)
btnOpenILGMS.grid(row=9, column=0)
btnOpenMFSearch.grid(row=9, column=1)
Label(window, text=" ").grid(row=10)
btnAbout.grid(row=11,column=0)
btnSettings.grid(row=11, column=1)


window.mainloop()
