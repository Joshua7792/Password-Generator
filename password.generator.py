#importing required libraries for TechVidvan Password Generator project using Python
from msilib.schema import CheckBox
import random
from tkinter import *
import string
import tkinter

# Creating a window
window = Tk()
window.title('TechVidvan')  # Window title
window.geometry('500x500')  # Window geometry

Label(window, font=('bold', 10), text='PASSWORD GENERATOR').pack()  # Giving label to window

# Function to generate password
def password_generate(leng):
    valid_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_'  # Characters of the password
    password = ''.join(random.sample(valid_char, leng))  # Random generation of password
    l = Label(window, text=password, font=('bold', 20))  # Displaying password
    l.place(x=190, y=50)

Checkbutton(text='4 character', onvalue=4, offvalue=0, variable=len1).place(x=200, y=150)  # Creating checkbox
Checkbutton(text='6 character', onvalue=6, offvalue=0, variable=len2).place(x=200, y=170)  # Creating checkbox
Checkbutton(text='8 character', onvalue=8, offvalue=0, variable=len3).place(x=200, y=190)  # Creating checkbox

# Converting string input to integer
len1 = tkinter.IntVar()
len2 = tkinter.IntVar()
len3 = tkinter.IntVar()

# Function to check the checkbox
def get_len():
    if len1.get() == 4:
        password_generate(4)
    elif len2.get() == 6:
        password_generate(6)
    elif len3.get() == 8:
        password_generate(8)
    else:
        password_generate(6)

Button(window, text='Generate', font=('normal', 10), bg='yellow', command=get_len).place(x=200, y=100)

window.mainloop()  # Run the window
