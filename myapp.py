import json
from tkinter import *

with open('users.json', 'r') as f:
    data = json.load(f)


class Login:
    def __init__(self):
        self.root = Tk()
        self.root.title('User Login')
        self.root.geometry('300x200')
        self.root.resizable(0, 0)

        self.label_un = Label(self.root, text='Username', font=("Arial", 14), padx=10, pady=10)
        self.label_un.grid(row=0, column=0)

        self.entry_un = Entry(self.root)
        self.entry_un.grid(row=0, column=1, padx=10)

        self.label_pw = Label(self.root, text='Password', font=("Arial", 14))
        self.label_pw.grid(row=1, column=0)

        self.entry_pw = Entry(self.root, show='*')
        self.entry_pw.grid(row=1, column=1)

        self.frame = Frame(self.root, padx=10, pady=20)
        self.frame.grid(row=2, column=0, columnspan=2)

        self.button_login = Button(self.frame, text='Login', width=10, command=self.login)
        self.button_login.pack(side='left')

        self.button_reg = Button(self.frame, text='Register', width=10)
        self.button_reg.pack(side='right')

        self.label_output = Label(self.root, padx=10, pady=20, text="", foreground='red')
        self.label_output.grid(row=3, column=0, columnspan=2)

        self.root.mainloop()

    def login(self):
        un = self.entry_un.get()
        pw = self.entry_pw.get()
        for user in data:
            if user['username'] == un and user['password'] == pw:
                auth_user_index = data.index(user)
                self.root.destroy()
                Transaction(auth_user_index)
                break
        else:
            self.label_output.config(text='Wrong Credentials')


class Transaction:
    def __init__(self, u):
        self.user = u

        self.root_db = Tk()
        self.root_db.title('User Dashboard')
        self.root_db.geometry('300x300')
        self.root_db.resizable(0, 0)

        global amount
        amount = StringVar()

        self.label_msg = Label(self.root_db, text=f'Welcome { data[self.user]["name"] }!!!',
                          font=("Arial", 14))
        self.label_msg.grid(row=0, column=0, padx=20)

        self.label_bal = Label(self.root_db,
                          text=f'Your Balance: NRs. { data[self.user]["balance"] }',
                          font=("Arial", 14))
        self.label_bal.grid(row=1, column=0, padx=20)

        self.btn_wd = Button(self.root_db, text="Withdraw", padx=5, pady=5,
                        command=lambda: self.transaction('withdraw'))
        self.btn_wd.grid(row=2, column=0, padx=20, pady=10)

        self.btn_dep = Button(self.root_db, text="Deposite", padx=5, pady=5,
                         command=lambda: self.transaction('deposite'))
        self.btn_dep.grid(row=3, column=0, padx=20)

        self.entry_amount = Entry(self.root_db, font=("Arial", 20), width=10,
                             justify='center', textvariable=amount)
        self.entry_amount.grid(row=4, column=0, padx=20, pady=10)

        self.root_db.mainloop()

    def transaction(self, opt):
        amt = float(self.entry_amount.get())
        if opt == 'withdraw':
            data[self.user]['balance'] = data[self.user]['balance'] - amt
        elif opt == 'deposite':
            data[self.user]['balance'] = data[self.user]['balance'] + amt

        self.entry_amount.delete(0, END)
        self.label_bal.config(text=f'Your Balance: NRs. { data[self.user]["balance"] }')

        with open('users.json', 'w') as f:
            json.dump(data, f)


Login()

