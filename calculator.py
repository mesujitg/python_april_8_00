from tkinter import *


class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title('Calculator')

        self.num1 = 0
        self.num2 = 0
        self.op = ''

        self.display = Entry(self.root, font=('Arial', '14'), width=15, justify='right')
        self.display.grid(row=0, column=0)

        # first key rows
        self.frame1 = Frame(self.root, padx=10)
        self.frame1.grid(row=1, column=0)

        self.btn7 = Button(self.frame1, text='7', padx=10, pady=5,
                           command=lambda: self.on_key_click(7))
        self.btn7.grid(row=0, column=0)

        self.btn8 = Button(self.frame1, text='8', padx=10, pady=5,
                           command=lambda: self.on_key_click(8))
        self.btn8.grid(row=0, column=1)

        self.btn9 = Button(self.frame1, text='9', padx=10, pady=5,
                           command=lambda: self.on_key_click(9))
        self.btn9.grid(row=0, column=2)

        self.btndiv = Button(self.frame1, text='/', padx=10, pady=5,
                             command=lambda: self.on_key_click('/'))
        self.btndiv.grid(row=0, column=3)

        # second key rows
        self.frame2 = Frame(self.root, padx=10)
        self.frame2.grid(row=2, column=0)

        self.btn4 = Button(self.frame2, text='4', padx=10, pady=5,
                           command=lambda: self.on_key_click(4))
        self.btn4.grid(row=0, column=0)

        self.btn5 = Button(self.frame2, text='5', padx=10, pady=5,
                           command=lambda: self.on_key_click(5))
        self.btn5.grid(row=0, column=1)

        self.btn6 = Button(self.frame2, text='6', padx=10, pady=5,
                           command=lambda: self.on_key_click(6))
        self.btn6.grid(row=0, column=2)

        self.btnmul = Button(self.frame2, text='x', padx=10, pady=5,
                             command=lambda: self.on_key_click('*'))
        self.btnmul.grid(row=0, column=3)

        # third key rows
        self.frame3 = Frame(self.root, padx=10)
        self.frame3.grid(row=3, column=0)

        self.btn1 = Button(self.frame3, text='1', padx=10, pady=5,
                           command=lambda: self.on_key_click(1))
        self.btn1.grid(row=0, column=0)

        self.btn2 = Button(self.frame3, text='2', padx=10, pady=5,
                           command=lambda: self.on_key_click(2))
        self.btn2.grid(row=0, column=1)

        self.btn3 = Button(self.frame3, text='3', padx=10, pady=5,
                           command=lambda: self.on_key_click(3))
        self.btn3.grid(row=0, column=2)

        self.btnsub = Button(self.frame3, text='-', padx=10, pady=5,
                             command=lambda: self.on_key_click('-'))
        self.btnsub.grid(row=0, column=3)

        # fourth key rows
        self.frame4 = Frame(self.root, padx=10)
        self.frame4.grid(row=4, column=0)

        self.btnc = Button(self.frame4, text='C', padx=10, pady=5,
                           command=lambda: self.on_key_click('c'))
        self.btnc.grid(row=0, column=0)

        self.btn0 = Button(self.frame4, text='0', padx=10, pady=5,
                           command=lambda: self.on_key_click(0))
        self.btn0.grid(row=0, column=1)

        self.btneq = Button(self.frame4, text='=', padx=10, pady=5,
                            command=lambda: self.on_key_click('='))
        self.btneq.grid(row=0, column=2)

        self.btnadd = Button(self.frame4, text='+', padx=10, pady=5,
                             command=lambda: self.on_key_click('+'))
        self.btnadd.grid(row=0, column=3)

        self.root.mainloop()

    def on_key_click(self, val):
        if val == 'c':
            self.display.delete(0, END)
        elif val == '+' or val == '-' or val == '/' or val == '*':
            self.num1 = float(self.display.get())
            self.op = val
            self.display.delete(0, END)
            print(self.num1, self.op)
        elif val == '=':
            self.num2 = float(self.display.get())
            self.display.delete(0, END)
            self.display.insert(0, self.calculate())
        else:
            self.display.insert(END, val)

    def calculate(self):
        if self.op == '+':
            return self.num1 + self.num2
        elif self.op == '-':
            return self.num1 - self.num2
        elif self.op == '*':
            return self.num1 * self.num2
        elif self.op == '/':
            return self.num1 / self.num2

    # dot(.)  backspace  +/-   sqrt


c = Calculator()
