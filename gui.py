from tkinter import *
from tkinter import ttk
import json


with open('users.json', 'r') as f:
    data = json.load(f)

print(data)

auth_user_index = None


root = Tk()
root.title('User Login')
root.geometry('300x200')
root.resizable(0, 0)


def transaction(opt):
    amt = float(amount.get())
    if opt == 'withdraw':
        data[auth_user_index]['balance'] = data[auth_user_index]['balance'] - amt
    elif opt == 'deposite':
        data[auth_user_index]['balance'] = data[auth_user_index]['balance'] + amt

    print('New Balance:', data[auth_user_index]['balance'])
    with open('users.json', 'w') as f:
        json.dump(data, f)


def on_login_click():
    global auth_user_index
    un = entry_un.get()
    pw = entry_pw.get()
    for user in data:
        if user['username'] == un and user['password'] == pw:
            print('Logged in')
            auth_user_index = data.index(user)
            root.destroy()

            root_db = Tk()
            root_db.title('User Dashboard')
            root_db.geometry('300x300')
            root_db.resizable(0, 0)

            global amount
            amount = StringVar()

            label_msg = Label(root_db, text=f'Welcome {user["name"]}!!!',
                              font=("Arial", 14))
            label_msg.grid(row=0, column=0, padx=20)

            label_bal = Label(root_db,
                              text=f'Your Balance: NRs. {user["balance"]}',
                              font=("Arial", 14))
            label_bal.grid(row=1, column=0, padx=20)

            btn_wd = Button(root_db, text="Withdraw", padx=5, pady=5,
                            command=lambda: transaction('withdraw'))
            btn_wd.grid(row=2, column=0, padx=20, pady=10)

            btn_dep = Button(root_db, text="Deposite", padx=5, pady=5,
                             command=lambda: transaction('deposite'))
            btn_dep.grid(row=3, column=0, padx=20)

            entry_amount = Entry(root_db, font=("Arial", 20), width=10,
                           justify='center', textvariable=amount)
            entry_amount.grid(row=4, column=0, padx=20, pady=10)

            root_db.mainloop()

            break
    else:
        print('Wrong Credentials')
        label_output.config(text='Wrong Credentials')



# grid, place, pack
label_un = Label(root, text='Username', font=("Arial", 14), padx=10, pady=10)
label_un.grid(row=0, column=0)

entry_un = Entry(root)
entry_un.grid(row=0, column=1, padx=10)

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

label_output = Label(root, padx=10, pady=20, text="", foreground='red')
label_output.grid(row=3, column=0, columnspan=2)

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


