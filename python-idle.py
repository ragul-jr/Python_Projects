from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename,askopenfilename
import subprocess
import os

root=Tk()
root.title("python idle")
root.geometry("1280x720+150+80")
root.configure(bg="#323846")

# image_icon=PhotoImage(file="")
# root.iconphoto(False,image_icon)

code_input =Text(root,font="coslas 18")
code_input .place(x=180,y=0,width=680,height=720)

code_input =Text(root,font="consolas 15",bg="#323846",fg="lightgreen")
code_input.place(x=860,y=0,width=420,height=720)

# open=PhotoImage(file="open.png")
# save=PhotoImage(file="save.png")
# run=PhotoImage("run.png")

# Button(root,image=open,bg="#323846",bd=0).place(x=30,y=30)
# Button(root,image=save,bg="#323846",bd=0).place(x=30,y=145)
# Button(root,image=run,bg="#323846",bd=0).place(x=30,y=260)



root.mainloop()