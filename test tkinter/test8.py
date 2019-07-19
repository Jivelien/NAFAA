import threading
import time
import tkinter
from tkinter import ttk


# in a real program it's best to use after callbacks instead of
# sleeping in a thread, this is just an example
def blocking_function():
    print("blocking function starts")
    time.sleep(1)
    print("blocking function ends")


def start_new_thread():
    thread = threading.Thread(target=blocking_function)
    thread.start()

def test(test):
    print('hello')
    
root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

label = ttk.Label(big_frame, text= 'test')
label.bind("<Button-1>", test)
button = ttk.Button(big_frame, text="Start the blocking function",
                    command=start_new_thread)
label.pack()
button.pack()
root.mainloop()