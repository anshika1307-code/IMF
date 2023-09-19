from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os 
import shutil
from tkinter import messagebox

def decryption_process():
   wlc.destroy()
   if (entry_var.get()==''):
       os.system("python keynotfound.py")
       wlc.destroy()
   else:
      isexist=os.path.exists("C:/Users/abhis/OneDrive/Desktop/Kavach2023/GUI/decrypt14_15")
      if not isexist:
       original = r"C:/Users/abhis/OneDrive/Desktop/Kavach2023/GUI/decrypt14_15.py"
       target = r"C:/Users/abhis/OneDrive/Desktop/Kavach2023/GUI/Collections/decrypt14_15.py"

      shutil.copyfile(original, target)
   import keyuploaded   





def upload_database():
    filepath=filedialog.askopenfilename()
    path="C:/Users/abhis/OneDrive/Desktop/Kavach2023/GUI/Collections"
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:

    # Create a new directory because it does not exist
     os.makedirs(path)
     print("The new directory is created!")
    original = filepath
    target = r"C:/Users/abhis/OneDrive/Desktop/Kavach2023/GUI/Collections/msgstore.db.crypt15"

    shutil.copyfile(original, target)
    messagebox.showinfo("Success", "Your database is Successfully Uploaded")

def upload_key():
    file_path1 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path1:
        with open(file_path1, "r") as file:
            file_data = file.read()
            entry_var.set(file_data)

    original = file_path1
    target = r"C:/Users/abhis/OneDrive/Desktop/Kavach2023/GUI/Collections/keyfile.key"

    shutil.copyfile(original, target)
    messagebox.showinfo("Success", "Your key is Successfully Uploaded")


def back_window():
   wlc.destroy()
   os.system('python welcome.py')

wlc=Tk()
wlc.geometry('1280x800+200+30')
wlc.title('Add Database')
bgwlc = PhotoImage(file='bg.png')
bgwlcLabel = Label(wlc, image=bgwlc)
bgwlcLabel.place(x=0, y=0)
bgwlcLabel.pack()

wlcframe = Frame(wlc, bg='white', width=140, height=100)
wlcframe.place(x=370, y=177)

proceedimage=Image.open("database.png")
resized=proceedimage.resize((550,120),Image.ANTIALIAS)
new_image=ImageTk.PhotoImage(resized)
proceedbutton = Button(wlcframe, image=new_image, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white',command=upload_database)
proceedbutton.place(x=370, y=177)
proceedbutton.pack()

wlcframe2 = Frame(wlc, bg='white', width=140, height=100)
wlcframe2.place(x=870, y=430)

proceedimage2=Image.open("uploadbtn.png")
resized2=proceedimage2.resize((250,50),Image.ANTIALIAS)
new_image2=ImageTk.PhotoImage(resized2)
proceedbutton2 = Button(wlcframe2, image=new_image2, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white',command=upload_database)
proceedbutton2.place(x=870, y=430)
proceedbutton2.pack()


btnframe2 = Frame(wlc, bg='white', width=140, height=100)
btnframe2.place(x=870, y=520)

proceedimagebtn2=Image.open("uploadbtn.png")
resizedbtn2=proceedimagebtn2.resize((250,50),Image.ANTIALIAS)
new_imagebtn2=ImageTk.PhotoImage(resizedbtn2)
proceedbuttonbtn2 = Button(btnframe2, image=new_imagebtn2, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white',command=upload_key)
proceedbuttonbtn2.place(x=870, y=520)
proceedbuttonbtn2.pack()

entry_var = StringVar()
keyupload = Entry(wlc, font=('times new roman', 13), bg='lightgray',textvariable=entry_var)
keyupload.place(x=855, y=620, width=300)




optionframe = Frame(wlc, bg='white', width=440, height=100)
optionframe.place(x=900, y=355)

options_list = ["     DingTalk     ", "     We-Chat     ", "     Whatsapp     "]
  
# Variable to keep track of the option
# selected in OptionMenu
value_inside = StringVar(wlc)
  
# Set the default value of the variable
value_inside.set("          Select an Option          ")
  
# Create the optionmenu widget and passing 
# the options_list and value_inside to it.
question_menu = OptionMenu(optionframe, value_inside, *options_list)
question_menu.pack()
  
# Function to print the submitted option-- testing purpose
  
  
def print_answers():
    print("Selected Option: {}".format(value_inside.get()))
    return None
  
  
# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose
submit_button = Button(wlc, text='Submit', command=print_answers)
submit_button.pack()

btnframe4 = Frame(wlc, bg='white', width=140, height=100)
btnframe4.place(x=570, y=680)

proceedimagebtn4=Image.open("next.png")
resizedbtn4=proceedimagebtn4.resize((150,50),Image.ANTIALIAS)
new_imagebtn4=ImageTk.PhotoImage(resizedbtn4)
proceedbuttonbtn4 = Button(btnframe4, image=new_imagebtn4, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white',command=decryption_process)
proceedbuttonbtn4.place(x=670, y=620)
proceedbuttonbtn4.pack()

btnframe5 = Frame(wlc, bg='white', width=140, height=100)
btnframe5.place(x=790, y=6)

proceedimagebtn5=Image.open("back.png")
resizedbtn5=proceedimagebtn5.resize((70,30),Image.ANTIALIAS)
new_imagebtn5=ImageTk.PhotoImage(resizedbtn5)
proceedbuttonbtn5 = Button(btnframe5, image=new_imagebtn5, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white',command=back_window)
proceedbuttonbtn5.place(x=790, y=6)
proceedbuttonbtn5.pack()


wlc.mainloop()