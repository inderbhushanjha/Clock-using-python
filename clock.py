import sys
from tkinter import *
import time


def clock1():
	time_str=time.strftime("%H:%M:%S")
	clock.config(text=time_str)
	clock.after(200,clock1)

root=Tk()
clock= Label(root,font={"times", 200, "bold"}, bg="white",fg="red")
clock.pack(fill=BOTH, expand=1)
clock1()
root.mainloop()