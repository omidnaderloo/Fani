
from tkinter import *

def login():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "admin" and password == "1234":
        result_label.config(text="ورود موفقیت‌آمیز بود ✅", fg="green")
    else:
        result_label.config(text="نام کاربری یا رمز اشتباه است ❌", fg="red")


win = Tk()
win.title("صفحه ورود")
win.geometry("1920x1080")
win.config(bg="#f0f0f0")


title_label = Label(win, text="ورود به سیستم", font=("Arial", 16), bg="#f0f0f0")
title_label.pack(pady=10)


user_label = Label(win, text="نام کاربری:", bg="#f0f0f0")
user_label.pack()
user_entry = Entry(win)
user_entry.pack(pady=5)


pass_label = Label(win, text="رمز عبور:", bg="#f0f0f0")
pass_label.pack()
pass_entry = Entry(win, show="*")
pass_entry.pack(pady=5)


login_button = Button(win, text="ورود", command=login, bg="#4CAF50", fg="white")
login_button.pack(pady=10)


result_label = Label(win, text="", bg="#f0f0f0", font=("Arial", 12))
result_label.pack()


win.mainloop()
