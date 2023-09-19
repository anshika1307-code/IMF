from tkinter import *
from PIL import Image, ImageTk
import os


def close():
    wlc.destroy()
    os.system('python adddatabase.py')

def open_chats():
    wlc.destroy()
    os.system('python representation.py')

wlc=Tk()
wlc.geometry('1000x700+200+30')
wlc.title('DECRYPTION SUCCESS')
bgwlc = PhotoImage(file='viewdatabase.png')
bgwlcLabel = Label(wlc, image=bgwlc)
bgwlcLabel.place(x=0, y=0)
bgwlcLabel.pack()

wlcframe2 = Frame(wlc, bg='white', width=140, height=100)
wlcframe2.place(x=900, y=120)

proceedimage2=Image.open("close.png")
resized2=proceedimage2.resize((20,20),Image.ANTIALIAS)
new_image2=ImageTk.PhotoImage(resized2)
proceedbutton2 = Button(wlcframe2, image=new_image2, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white',command=close)
proceedbutton2.place(x=900, y=120)
proceedbutton2.pack()

decryptframe = Frame(wlc, bg='white', width=140, height=100)
decryptframe.place(x=100, y=320)

decryptimage=Image.open("viewbtn.png")
resized=decryptimage.resize((370,130),Image.ANTIALIAS)
new_image=ImageTk.PhotoImage(resized)
decryptbutton = Button(decryptframe, image=new_image, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white',command=open_chats)
decryptbutton.place(x=100, y=320)
decryptbutton.pack()

decryptframe1 = Frame(wlc, bg='white', width=140, height=100)
decryptframe1.place(x=530, y=320)

decryptimage1=Image.open("differentkey.png")
resized1=decryptimage1.resize((370,130),Image.ANTIALIAS)
new_image1=ImageTk.PhotoImage(resized1)
decryptbutton1 = Button(decryptframe1, image=new_image1, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white')
decryptbutton1.place(x=530, y=320)
decryptbutton1.pack()

wlc.mainloop()