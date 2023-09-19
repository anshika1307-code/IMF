from tkinter import *
from PIL import Image, ImageTk
import os
import subprocess
from tkinter import messagebox

def close():
    wlc.destroy()
    os.chdir("C:/Users/abhis/OneDrive/Desktop/Kavach2023/GUI")
    os.system('python adddatabase.py')

def decryption():
      filepath="C:/Users/abhis/OneDrive/Desktop/Kavach2023/GUI/Collections/keyfile.key"
      with open(filepath, "r") as file:
            file_data = file.read()
      

      # Replace 'directory_path', 'filepath', and 'additional_text' with your actual paths and text
      directory_path = "C:/Users/abhis/OneDrive/Desktop/Kavach2023/GUI/Collections"
      file__path = "C:/Users/abhis/OneDrive/Desktop/Kavach2023/GUI/Collections/decrypt14_15.py"

      # Change the current directory
      try:
         os.chdir(directory_path)
      except OSError as e:
           print(f"Failed to change directory: {e}")
           exit(1)

      # Construct the command to run
      command = f"python {file__path} {file_data}"

      # Use subprocess to run the command
      try:
        subprocess.run(command, shell=True, check=True)
        messagebox.showinfo("Success","your database is successfullly decrypted")
        # Change the current directory
        directory_path1="C:/Users/abhis/OneDrive/Desktop/Kavach2023/GUI"
        try:
          os.chdir(directory_path1)
        except OSError as e:
           print(f"Failed to change directory: {e}")
           exit(1)
        wlc.destroy()   
        os.system('python viewdatabase.py')
        
      except subprocess.CalledProcessError as e:
           print(f"An error occurred: {e}")
           messagebox.showerror("Error",e)

wlc=Tk()
wlc.geometry('1000x700+200+30')
wlc.title('Key Found')
bgwlc = PhotoImage(file='keyuploaded.png')
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
decryptframe.place(x=320, y=320)

decryptimage=Image.open("decryptbtn.png")
resized=decryptimage.resize((370,130),Image.ANTIALIAS)
new_image=ImageTk.PhotoImage(resized)
decryptbutton = Button(decryptframe, image=new_image, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white',command=decryption)
decryptbutton.place(x=320, y=320)
decryptbutton.pack()

wlc.mainloop()