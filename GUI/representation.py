from tkinter import *
from PIL import Image, ImageTk
import sqlite3

def populate_table(data, inner_frame):
     # Create table header
        header = ["Recieved", "Sent",""]
        for j in range(len(header)):
            label = Label(inner_frame, text=header[j], borderwidth=1, relief="solid", width=56, height=2)
            label.grid(row=0, column=j)

        #creating grids
        for i in range(len(data)):
            for j in range(len(data[i])):
                label.grid(row=i + 1, column=j)
                label = Label(inner_frame, borderwidth=1, relief="solid", width=56, height=2)
        

        # Create table rows
        for i in range(len(data)):
            for j in range(len(data[i])):
                if (data[i][-1]!=-1):
                  cell_data = data[i][1]
                  if (cell_data!=None):
                    label = Label(inner_frame, text=cell_data, borderwidth=1, relief="solid", width=56, height=2)
                    label.grid(row=i + 1, column=1)
                    

            if data[i][-1] == -1:
             cell_data = data[i][0]
             if (cell_data!=None):
                 label = Label(inner_frame, text=cell_data, borderwidth=1, relief="solid", width=56, height=2)
                 label.grid(row=i + 1, column=0)

def create_table():
        conn = sqlite3.connect("C:/Users/abhis/OneDrive/Desktop/Kavach2023\GUI/Collections/msgstore.db")
        cursor = conn.cursor()

        # Fetch data from the database
        cursor.execute("SELECT text_data,text_data, receipt_server_timestamp FROM message WHERE text_data IS NOT NULL")
        data = cursor.fetchall()

        # Close the database connection
        cursor.close()
        conn.close()
        return data

    

def on_frame_configure(event, canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_canvas_configure(event, canvas):
    canvas.itemconfig(canvas.find_withtag("window"), width=event.width)

wlc=Tk()
wlc.geometry('1280x800+200+30')
wlc.title('Representation')
bgwlc = PhotoImage(file='representation.png')
bgwlcLabel = Label(wlc, image=bgwlc)
bgwlcLabel.place(x=0, y=0)
bgwlcLabel.pack()

frame = Frame(wlc, bg='grey', width='810', height='360')
frame.pack()
frame.pack_propagate(0)
frame.place(x=360, y=345)

canvas = Canvas(frame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scroll_y = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
scroll_y.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scroll_y.set)

inner_frame = Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor=NW)

data=create_table()
populate_table(data, inner_frame)

inner_frame.bind("<Configure>", lambda event, canvas=canvas: on_frame_configure(event, canvas))
canvas.bind("<Configure>", lambda event, canvas=canvas: on_canvas_configure(event, canvas))

wlc.mainloop()

