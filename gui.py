from tkinter import *
from tkinter import ttk

root = Tk()
root.title('User Login')
root.geometry('300x300')
# root.resizable(0, 0)


def on_login_click():
    # un = entry_un.get()
    # pw = entry_pw.get()
    # entry_un.insert(0, combo.get())
    # label_output.config(text=un)
    print(un.get())


un = StringVar()
pw = StringVar()
gender = StringVar()


# grid, place, pack
label_un = Label(root, text='Username', font=("Arial", 14), padx=10, pady=10)
label_un.grid(row=0, column=0)

entry_un = Entry(root, textvariable=un)
entry_un.grid(row=0, column=1)

label_pw = Label(root, text='Password', font=("Arial", 14))
label_pw.grid(row=1, column=0)

entry_pw = Entry(root, show='*', textvariable=pw)
entry_pw.grid(row=1, column=1)

frame = Frame(root, padx=10, pady=20)
frame.grid(row=2, column=0, columnspan=2)

button_login = Button(frame, text='Login', width=10, command=on_login_click)
button_login.pack(side='left')

button_reg = Button(frame, text='Register', width=10)
button_reg.pack(side='right')

# label_output = Label(root, padx=10, pady=20, text="Output")
# label_output.grid(row=3, column=0, columnspan=2)
#
# radio_male = Radiobutton(root, text='Male', textvariable=gender, value='Male')
# radio_male.grid(row=4, column=0)
# radio_female = Radiobutton(root, text='Female', textvariable=gender, value='Female')
# radio_female.grid(row=4, column=1)
# radio_other = Radiobutton(root, text='Other', textvariable=gender, value='Other')
# radio_other.grid(row=4, column=2)
#
# combo = ttk.Combobox(root, values=('Nepal', 'India', 'China'), state='readonly')
# combo.grid(rows=5, column=0, columnspan=2)
#
# textarea = Text(root, height=5, width=15)
# textarea.grid(rows=6, column=0, columnspan=2)
#
# check_music = Checkbutton(root, text='Music')
# check_music.grid(rows=7, column=0)
# check_travel = Checkbutton(root, text='Travel')
# check_travel.grid(rows=7, column=1)
# check_photography = Checkbutton(root, text='Photography')
# check_photography.grid(rows=7, column=2)

root.mainloop()


