from tkinter import * 

def board():
    top= Tk()
    top.geometry("200x200")
    c = Canvas(top,bg = 'white', height="200")
    c.pack()
    top.mainloop()