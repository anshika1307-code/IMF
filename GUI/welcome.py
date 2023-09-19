from tkinter import *
from PIL import Image, ImageTk



def upload_database():
    wlc.destroy()
    import adddatabase


def extract_database1():
    wlc.destroy()
    import extractdatabase


wlc=Tk()
wlc.geometry('1280x800+200+30')
wlc.title('welcome')
bgwlc = PhotoImage(file='home.png')
bgwlcLabel = Label(wlc, image=bgwlc)
bgwlcLabel.place(x=0, y=0)
bgwlcLabel.pack()

wlcframe = Frame(wlc, bg='white', width=140, height=100)
wlcframe.place(x=900, y=277)

proceedimage=Image.open("upload.png")
resized=proceedimage.resize((250,120),Image.ANTIALIAS)
new_image=ImageTk.PhotoImage(resized)
proceedbutton = Button(wlcframe, image=new_image, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white',command=upload_database)
proceedbutton.place(x=900, y=277)
proceedbutton.pack()

wlcframe1 = Frame(wlc, bg='white', width=140, height=100)
wlcframe1.place(x=900, y=420)

proceedimage1=Image.open("extract.png")
resized1=proceedimage1.resize((250,120),Image.ANTIALIAS)
new_image1=ImageTk.PhotoImage(resized1)
proceedbutton1 = Button(wlcframe1, image=new_image1, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white',command=extract_database1)
proceedbutton1.place(x=900, y=420)
proceedbutton1.pack()


home= Label(wlc, text='Home', font=('Arial', 12, 'bold'),
                       fg='gray20', )
home.place(x=900, y=10)


About= Label(wlc, text='About', font=('Arial', 12, 'bold'),fg='gray20', )
About.place(x=980, y=10)

logout = Frame(wlc, bg='white', width=100, height=100)
logout.place(x=1060, y=10)

proceedimage3=Image.open("logout.png")
resized3=proceedimage3.resize((70,25),Image.ANTIALIAS)
new_image3=ImageTk.PhotoImage(resized3)
logoutbutton = Button(logout, image=new_image3, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white')
logoutbutton.place(x=1060, y=10)
logoutbutton.pack()


wlc.mainloop()
