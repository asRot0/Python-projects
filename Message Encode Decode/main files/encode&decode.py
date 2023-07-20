# import tkinter module
from tkinter import *

# import other necessary modules
import random
import time
import datetime

# Vigenère cipher
import base64

# creating root object
root = Tk()

# defining size of window
root.geometry("1200x800")

# setting up the title of window
root.title("Message Encryption and Decryption")

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700,
           relief=SUNKEN)
f1.pack(side=LEFT)


# function to update the time
def update_time():
    current_time = time.strftime("%d %b %Y %I:%M:%S %p %A", time.localtime())
    lblInfo.config(text=current_time)
    lblInfo.after(1000, update_time)  # update every 1000 milliseconds (1 second)


localtime = time.strftime("%d, %b %Y %I:%M:%S %p %A", time.localtime())

# Define the font styles
font_style = ('Georgia', 30, 'bold')
italic_font_style = ('Georgia', 20, 'italic')

# Create the first label with bold style
lblInfo_main = Label(Tops, font=font_style, text="SECRET MESSAGING")
lblInfo_main.grid(row=0, column=0)

# Create the second label with italic style
lblInfo_vigenere = Label(Tops, font=italic_font_style, text="Vigenère cipher", fg="Dark Orange", bd=5, anchor='w')
lblInfo_vigenere.grid(row=1, column=0)

# Adjust column weights to align the two labels
Tops.columnconfigure(0, weight=1)
Tops.columnconfigure(1, weight=1)

lblInfo = Label(Tops, font=('arial', 20, 'bold'),
                text=localtime, fg="Steel Blue",
                bd=10, anchor='w')

lblInfo.grid(row=2, column=0)

# update the time initially
update_time()

Msg = StringVar()
key = StringVar()
mode = StringVar()


# exit function
def qExit():
    root.destroy()


# Function to reset the window
def Reset():
    Msg.set("")
    key.set("")
    mode.set("")
    txtMsg.delete('1.0', 'end')
    txtService.config(state='normal')
    txtService.delete('1.0', 'end')


# labels

lblMsg = Label(f1, font=('arial', 16, 'bold'),
               text="MESSAGE", bd=16, anchor="w")

lblMsg.grid(row=0, column=0)

txtMsg = Text(f1, font=('arial', 10, 'bold'), wrap='word', width=35, height=5)
txtMsg.grid(row=0, column=1)

lblkey = Label(f1, font=('arial', 16, 'bold'),
               text="KEY", bd=16, anchor="w")

lblkey.grid(row=1, column=0)

txtkey = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=key, bd=10, insertwidth=4,
               bg="powder blue", justify='right')

txtkey.grid(row=1, column=1)

lblmode = Label(f1, font=('arial', 16, 'bold'),
                text="MODE(e for encrypt, d for decrypt)",
                bd=16, anchor="w")

lblmode.grid(row=2, column=0)

txtmode = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=mode, bd=10, insertwidth=4,
                bg="powder blue", justify='right')

txtmode.grid(row=2, column=1)

lblService = Label(f1, font=('arial', 16, 'bold'),
                   text="The Result-", bd=16, anchor="w")

lblService.grid(row=1, column=2)

txtService = Text(f1, font=('arial', 10, 'bold'), wrap='word', width=35, height=10,
                  state='disabled')

txtService.grid(row=0, column=3, rowspan=3)


# Function to encode
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256)

        enc.append(enc_c)

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# Function to decode
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
    return "".join(dec)


def Ref():
    clear = txtMsg.get("1.0", "end-1c")  # Retrieve the entire content of the Text widget
    print("message= ", clear)  # Retrieve the entire content of the Text widget
    k = key.get()
    m = mode.get()
    txtService.config(state='normal')
    txtService.delete('1.0', 'end')  # Clear the Text widget
    if m == 'e':
        txtService.insert("1.0", encode(k, clear))
    else:
        txtService.insert("1.0", decode(k, clear))
    txtService.config(state='disabled')


# Show message button
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black",
                  font=('arial', 16, 'bold'), width=10,
                  text="Show Message", bg="powder blue",
                  command=Ref).grid(row=7, column=1)

# Reset button
btnReset = Button(f1, padx=16, pady=8, bd=16,
                  fg="black", font=('arial', 16, 'bold'),
                  width=10, text="Reset", bg="green",
                  command=Reset).grid(row=7, column=2)

# Exit button
btnExit = Button(f1, padx=16, pady=8, bd=16,
                 fg="black", font=('arial', 16, 'bold'),
                 width=10, text="Exit", bg="red",
                 command=qExit).grid(row=7, column=3)

# keeps window alive
root.mainloop()
