#!/usr/bin/env python3
from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from tkinter import filedialog as fdialogue

from encrypt import encrypt
from decrypt import decrypt
from keygen import keygen
from ttkthemes import ThemedTk


root = ThemedTk(theme="black")
root.configure(bg="#414141")
root.title("DeepCrypt")

mainFrame = Frame(root)
mainFrame.grid()


def closeMainFrame():
    root.destroy()

def displayHelp():
    helpWindow = Toplevel(root)
    helpWindow.configure(bg="#414141")
    helpWindow.title("Help")

    def closeHelpWindow():
        helpWindow.destroy()

    Label(helpWindow, text="To encrypt a file, select \"Encrypt\", then your file, and then the key to encrypt with.").grid(column=1, row=1)
    Label(helpWindow, text="To decrypt a file, select \"Decrypt\", then your file, then the key to decrypt with.").grid(column=1, row=2)
    Label(helpWindow, text="Don't have an encryption key? Generate one with \"Generate Key\". Name it, and find it in "
                           "the \"Keys\" folder.").grid(column=1, row=3)
    Label(helpWindow, text="Keep this key in a safe place, but don't lose it -- without it, you can never decrypt "
                           "your files.").grid(column=1, row=4)

def displayLicense():
    licenseWindow = Toplevel(root)
    licenseWindow.configure(bg="#414141")
    licenseWindow.title("License")

    def closeLicenseWindow():
        licenseWindow.destroy()

    Label(licenseWindow, text="This program is licensed under the GNU GPL v3\nTo view the full license, "
                              "go to https://www.gnu.org/licenses/gpl-3.0.en.html").grid(column=1, row=1)
    Label(licenseWindow, text="THIS PROGRAM IS DISTRIBUTED AS IS, WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR\n "
                              "IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND\n "
                              "FITNESS FOR A PARTICULAR PURPOSE").grid(column=1, row=2)

def displayCredits():
    creditsWindow = Toplevel(root)
    creditsWindow.configure(bg="#414141")
    creditsWindow.title("Credits")

    def closeCreditsWindow():
        creditsWindow.destroy()

    Label(creditsWindow, text="Connor McDermid").grid(column=1, row=1)
    Label(creditsWindow, text="connor.mcdermid@mcvts.org").grid(column=2, row=1)
    Label(creditsWindow, text="Justin Ecarma").grid(column=1, row=2)
    Label(creditsWindow, text="justin.ecarma@mcvts.org").grid(column=2, row=2)
    Label(creditsWindow, text="Ian Elias").grid(column=1, row=3)
    Label(creditsWindow, text="ian.elias@mcvts.org").grid(column=2, row=3)
    Label(creditsWindow, text="Sudarshan Surendranathan").grid(column=1, row=4)
    Label(creditsWindow, text="shiddha4@gmail.com").grid(column=2, row=4)

def encryptButtonClicked():
    filename = askopenfilename(initialdir="./", title="Select a File",
                               filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    key_file = askopenfilename(initialdir="keys/", title="Select a Key",
                               filetypes=(("Key Files", "*.key*"), ("All Files", "*.*")))
    encrypt(filename, key_file)


def decryptButtonClicked():
    filename = askopenfilename(initialdir="./", title="Select a File",
                               filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    key_file = askopenfilename(initialdir="keys/", title="Select a Key",
                               filetypes=(("Key Files", "*.key*"), ("All Files", "*.*")))
    decrypt(filename, key_file)


def keygenButtonClicked():
    top = Toplevel(root)
    top.configure(bg="#414141")
    top.title("Key Generation")

    def closeKeyGenWindow():
        top.destroy()
        keygen(textEntry.get())

    textEntry = StringVar()

    e = Entry(top, textvariable=textEntry, width=10)

    Label(top, text="Enter your key's name").grid(column=1, row=1)
    e.grid(column=1, row=2)
    confirm_button = Button(top, text="Confirm", command=closeKeyGenWindow, )
    confirm_button.grid(column=1, row=3)


encrypt_button = Button(root, text="Encrypt", command=encryptButtonClicked)
decrypt_button = Button(root, text="Decrypt", command=decryptButtonClicked)
keygen_button = Button(root, text="Generate Key", command=keygenButtonClicked)
help_button = Button(root, text="Help", command=displayHelp)
license_button = Button(root, text="License", command=displayLicense)
authors_button = Button(root, text="Credits", command=displayCredits)

encrypt_button.grid(column=1, row=1)
decrypt_button.grid(column=2, row=1)
keygen_button.grid(column=1, row=2)
help_button.grid(column=2, row=2)
license_button.grid(column=1, row=3)
authors_button.grid(column=2, row=3)

root.mainloop()
