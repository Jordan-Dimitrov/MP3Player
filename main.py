import imp
from msilib.schema import Directory
from tkinter import filedialog
from tkinter import *
import os
from turtle import title
from pygame import mixer
root = Tk()
root.config(bg="grey")
root.title("MP3")
listbox = Listbox(width=70, height=20, bg="cyan")
paused = False
onLoop = False
volume = 0.5
def load():
    directory = filedialog.askdirectory()
    os.chdir(directory)
    song_list = os.listdir()
    pos = 1

    for song in song_list:
        listbox.insert(pos,  song)
        pos+=1
def increase():
    global volume
    mixer.init
    if volume<1:
        volume+=0.1
    mixer.music.set_volume(volume)

def decrease():
    global volume
    mixer.init
    if volume>0:
        volume-=0.1
    mixer.music.set_volume(volume)

def play():
    mixer.init()
    mixer.music.load(listbox.get(listbox.curselection()))
    mixer.music.play()
def loop():
    global onLoop

    if onLoop == False:
        mixer.init()
        mixer.music.load(listbox.get(listbox.curselection()))
        mixer.music.play(-1)

def pause():
    global paused

    if paused == False:
        mixer.music.pause()
        paused=True
    elif paused == True:
        mixer.music.unpause()
        paused=False

def stop():
    mixer.music.stop()

load_button = Button(text="load", width=10,bg="blue", command=load)
load_button.pack(side="left")

increase_button = Button(text="increase vol", width=10,bg="purple", command=increase)
increase_button.pack(side="right")

decrease_button = Button(text="decrease vol", width=10,bg="pink", command=decrease)
decrease_button.pack(side="right")

loop_button = Button(text="loop", width=10,bg="orange", command=loop)
loop_button.pack(side="bottom")

stop_button = Button(text="stop", width=10,bg="red", command=stop)
stop_button.pack(side="bottom")

pause_button = Button(text="pause", width=10,bg="yellow", command=pause)
pause_button.pack(side="bottom")

play_button = Button(text="play", width=10,bg="green", command=play)
play_button.pack(side="bottom")

listbox.pack(side="right")

root.mainloop()