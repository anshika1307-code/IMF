from tkinter import *
from PIL import Image, ImageTk
import subprocess

def open_terminal():

    # Check the operating system and set the appropriate command
    command = 'cmd'

    if command:
        subprocess.run(command, shell=True)
    else:
        print("Unsupported operating system.")

wlc=Tk()
wlc.geometry('1280x800+200+30')
wlc.title('Add Database')
bgwlc = PhotoImage(file='extractwindow.png')
bgwlcLabel = Label(wlc, image=bgwlc)
bgwlcLabel.place(x=0, y=0)
bgwlcLabel.pack()

wlcframe = Frame(wlc, bg='white', width=140, height=100)
wlcframe.place(x=120, y=300)

proceedimage=Image.open("phone.png")
resized=proceedimage.resize((300,420),Image.ANTIALIAS)
new_image=ImageTk.PhotoImage(resized)
proceedbutton = Button(wlcframe, image=new_image, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white',command=open_terminal)
proceedbutton.place(x=120, y=300)
proceedbutton.pack()

wlcframe1 = Frame(wlc, bg='white', width=140, height=100)
wlcframe1.place(x=500, y=300)

proceedimage1=Image.open("cloud.png")
resized1=proceedimage1.resize((300,420),Image.ANTIALIAS)
new_image1=ImageTk.PhotoImage(resized1)
proceedbutton1 = Button(wlcframe1, image=new_image1, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white')
proceedbutton1.place(x=500, y=300)
proceedbutton1.pack()

wlcframe2 = Frame(wlc, bg='white', width=140, height=100)
wlcframe2.place(x=900, y=300)

proceedimage2=Image.open("pc.png")
resized2=proceedimage2.resize((300,420),Image.ANTIALIAS)
new_image2=ImageTk.PhotoImage(resized2)
proceedbutton2 = Button(wlcframe2, image=new_image2, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white')
proceedbutton2.place(x=900, y=300)
proceedbutton2.pack()

wlc.mainloop()