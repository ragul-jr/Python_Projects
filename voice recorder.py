from tkinter import *
from tkinter import messagebox
import sounddevice as sound
import scipy.io.wavfile import write
import time
import wavio as wv

root =Tk()
root.geometry("600x700+400+80")
root.resizable(False,False)
root.title("voice")
root.config(background="#4a4a4a")

def Record(){
    freq=44100
    dur=int(duration.get())
    recording=sound.rec(dur*freq,samplerate=freq,channels=2)

    try:
    temp=intz(duration.get())
    except:
    print("please enter the right value")

    while temp>0
    root.update()
    time.sleep(1)

    if (temp==0):
        messagebox.showinfo("time countdown","time s up")
    Label(text=f"{str(temp)}",font="arial 40",width=4,background="#4a4a4a").Place(x=240,y=590)  

    sound.wait()
    write("recording.wav",freq,recording)
}

Label(text="voice recorder",font="airal 30 bold",background="#4a4a4a",fg="white").pack()

duration =StringVar()
entry=Entry(root,textvariable=duration,font="arial 15",background="#4a4a4a"fg="white").pack(pady=10)
Label(text="enter time in seconds",font="arial 15",background="#4a4a4a",fg="white").pack()

record=Button(root,font="arial 20",text="record",bg="#111111",fg="white",border=0,command=Record).pack(Pady=30)



root.mainloop()