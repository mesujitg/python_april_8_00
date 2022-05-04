# my_num = 100

# def add():
#     a = int(input('Enter first number'))
#     b = int(input('Enter second number'))
#     print(a, '+', b, '=', a+b)

# add()


# def add_p(a, b, op):
#     print(a, '+', b, '=', a+b)

# num1 = int(input('Enter first number'))
# num2 = int(input('Enter first number'))
# add_p(num1, num2)


def calculate(a, b, op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b

num1 = float(input('Enter first number'))
oper = input('Enter first number')
num2 = float(input('Enter second number'))
print(calculate(num1, num2, oper))
