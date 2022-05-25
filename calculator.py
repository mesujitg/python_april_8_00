from tkinter import *
from math import sqrt


class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title('Calculator')

        self.num1 = 0
        self.num2 = 0
        self.op = ''

        self.display = Entry(self.root, font=('Arial', '14'), width=20, justify='right')
        self.display.grid(row=0, column=0, padx=20, pady=20)

        # first key rows
        self.frame1 = Frame(self.root, padx=10)
        self.frame1.grid(row=1, column=0, pady=2)

        self.btn7 = Button(self.frame1, text='7', width=5, height=2,
                           command=lambda: self.on_key_click(7))
        self.btn7.grid(row=0, column=0)

        self.btn8 = Button(self.frame1, text='8', width=5, height=2,
                           command=lambda: self.on_key_click(8))
        self.btn8.grid(row=0, column=1)

        self.btn9 = Button(self.frame1, text='9', width=5, height=2,
                           command=lambda: self.on_key_click(9))
        self.btn9.grid(row=0, column=2)

        self.btndiv = Button(self.frame1, text='/', width=5, height=2,
                             command=lambda: self.on_key_click('/'))
        self.btndiv.grid(row=0, column=3)

        # second key rows
        self.frame2 = Frame(self.root, padx=10)
        self.frame2.grid(row=2, column=0, pady=2)

        self.btn4 = Button(self.frame2, text='4', width=5, height=2,
                           command=lambda: self.on_key_click(4))
        self.btn4.grid(row=0, column=0)

        self.btn5 = Button(self.frame2, text='5', width=5, height=2,
                           command=lambda: self.on_key_click(5))
        self.btn5.grid(row=0, column=1)

        self.btn6 = Button(self.frame2, text='6', width=5, height=2,
                           command=lambda: self.on_key_click(6))
        self.btn6.grid(row=0, column=2)

        self.btnmul = Button(self.frame2, text='x', width=5, height=2,
                             command=lambda: self.on_key_click('*'))
        self.btnmul.grid(row=0, column=3)

        # third key rows
        self.frame3 = Frame(self.root, padx=10)
        self.frame3.grid(row=3, column=0, pady=2)

        self.btn1 = Button(self.frame3, text='1', width=5, height=2,
                           command=lambda: self.on_key_click(1))
        self.btn1.grid(row=0, column=0)

        self.btn2 = Button(self.frame3, text='2', width=5, height=2,
                           command=lambda: self.on_key_click(2))
        self.btn2.grid(row=0, column=1)

        self.btn3 = Button(self.frame3, text='3', width=5, height=2,
                           command=lambda: self.on_key_click(3))
        self.btn3.grid(row=0, column=2)

        self.btnsub = Button(self.frame3, text='-', width=5, height=2,
                             command=lambda: self.on_key_click('-'))
        self.btnsub.grid(row=0, column=3)

        # fourth key rows
        self.frame4 = Frame(self.root, padx=10)
        self.frame4.grid(row=4, column=0, pady=2)

        self.btnc = Button(self.frame4, text='C', width=5, height=2,
                           command=lambda: self.on_key_click('c'))
        self.btnc.grid(row=0, column=0)

        self.btn0 = Button(self.frame4, text='0', width=5, height=2,
                           command=lambda: self.on_key_click(0))
        self.btn0.grid(row=0, column=1)

        self.btneq = Button(self.frame4, text='=', width=5, height=2,
                            command=lambda: self.on_key_click('='))
        self.btneq.grid(row=0, column=2)

        self.btnadd = Button(self.frame4, text='+', width=5, height=2,
                             command=lambda: self.on_key_click('+'))
        self.btnadd.grid(row=0, column=3)

        # fifth key rows
        self.frame5 = Frame(self.root, padx=10)
        self.frame5.grid(row=5, column=0, pady=2)

        self.btnsign = Button(self.frame5, text='+/-', width=5, height=2,
                           command=lambda: self.on_key_click('+/-'))
        self.btnsign.grid(row=0, column=0)

        self.btndot = Button(self.frame5, text='.', width=5, height=2,
                           command=lambda: self.on_key_click('.'))
        self.btndot.grid(row=0, column=1)

        self.btnbs = Button(self.frame5, text='<--', width=5, height=2,
                            command=lambda: self.on_key_click('<--'))
        self.btnbs.grid(row=0, column=2)

        self.btnsqrt = Button(self.frame5, text='SqRt', width=5, height=2,
                             command=lambda: self.on_key_click('SqRt'))
        self.btnsqrt.grid(row=0, column=3)

        self.root.mainloop()

    def on_key_click(self, val):
        if val == 'c':
            self.display.delete(0, END)
        elif val == '+' or val == '-' or val == '/' or val == '*' or val == 'SqRt':
            self.num1 = float(self.display.get())
            self.op = val
            self.display.delete(0, END)
            if val == 'SqRt':
                result = sqrt(self.num1)
                self.display.insert(0, result)
        elif val == '=':
            self.num2 = float(self.display.get())
            self.display.delete(0, END)
            self.display.insert(0, self.calculate())
        elif val == '+/-':
            if self.display.get()[0] == '-':
                self.display.delete(0)
            else:
                self.display.insert(0, '-')
        else:
            if val == 0 and self.display.get() == '':
                pass
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
