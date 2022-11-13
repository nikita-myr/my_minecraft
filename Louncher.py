from tkinter import *
from tkinter import ttk
import os

# create louncher window
Louncher = Tk(className='Louncher for my minecraft')

def start_game():
    Louncher.destroy
    os.system('cd /Users/nikita/Dev/Python_projects/my_minecraft')
    os.system('python3 main.py')


# window size settings
Louncher.geometry('800x600')
Louncher.resizable(False, False)


# walpapper image
walpapper = PhotoImage(file='/Users/nikita/Dev/Python_projects/my_minecraft/walpapper.png')
label_walpapper = Label(Louncher, image=walpapper)
label_walpapper.place(x=0, y=0)

start_button = ttk.Button(Louncher, text='Start game', command=lambda: start_game())
start_button.place(x=350, y=200)

quit_button = ttk.Button(Louncher, text='Quit', command=Louncher.destroy)
quit_button.place(x=360, y=400)




Louncher.mainloop()
