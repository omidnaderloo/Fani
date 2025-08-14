from tkinter import *

def change():
    matn.config(text="hello",fg="red")
    win.config(bg="green")
    change_but.config(width=40)

win=Tk()
win.geometry("1920x1080")
matn=Label(win,text="welcome")
matn.pack()
change_but=Button(win,text="change",command=change)
change_but.pack()

win.mainloop()