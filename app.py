import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()


intro = messagebox.showinfo("Message for you", "Hello there")
messagebox.showinfo("Message for you", "I have a question for you")

while True:
    result = messagebox.askyesno("Important message", "Will you be my valentine?")
    if result == True:
        messagebox.showinfo("Hehehe thanks","I knew you'd say yes! I'm hard to say no to(lol). Here's my number: XXXXXXXXXX")
        break
    else:
        messagebox.showerror("Not allowed!", "I'll keep asking till you say yes!")
