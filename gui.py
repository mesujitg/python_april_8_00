from tkinter import *

root = Tk()
root.title('User Login')
root.geometry('300x300')
# root.resizable(0, 0)


def on_login_click():
    un = entry_un.get()
    pw = entry_pw.get()
    entry_pw.insert(0, un)
    label_ouptput.config(text=un)
    print(un, pw)


# grid, place, pack
label_un = Label(root, text='Username', font=("Arial", 14), padx=10, pady=10)
label_un.grid(row=0, column=0)

entry_un = Entry(root)
entry_un.grid(row=0, column=1)

label_pw = Label(root, text='Password', font=("Arial", 14))
label_pw.grid(row=1, column=0)

entry_pw = Entry(root, show='*')
entry_pw.grid(row=1, column=1)

frame = Frame(root, padx=10, pady=20)
frame.grid(row=2, column=0, columnspan=2)

button_login = Button(frame, text='Login', width=10, command=on_login_click)
button_login.pack(side='left')

button_reg = Button(frame, text='Register', width=10)
button_reg.pack(side='right')

label_ouptput = Label(root, padx=10, pady=20, text="Output")
label_ouptput.grid(row=3, column=0, columnspan=2)

root.mainloop()


