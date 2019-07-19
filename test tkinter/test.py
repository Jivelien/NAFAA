#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:02:44 2019

@author: jude
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import time
import functools

root = tk.Tk()

big_frame = tk.Frame(root)
big_frame.pack(fill='both', expand=True)


def stupid_callback():
    time.sleep(5)
        
def change_text():
    if label['text'] == 'Hello':
        label['text'] = 'World'
    else:
        label['text'] = 'Hello'

def print_hello_number(number):
    print("hello", number)
    
label = ttk.Label(big_frame, text="This is a button test.")
label.pack()
button = ttk.Button(big_frame, text="Click me!", command=change_text)
button.pack()
i=5
button2 = ttk.Button(big_frame, text="This sucks", command=functools.partial(print_hello_number, i))
button2.pack()


    
root.title("Button Test")
root.geometry('200x100')
root.minsize(150, 50)
root.resizable(False, False)
root.mainloop()