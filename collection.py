# students_list = ['ram', 'shyam', 'hari', 'krish', 'john', 'shyam']
# students_tuple = ('ram', 'shyam', 'hari', 'krish', 'john', 'shyam')
# students_set = {'ram', 'shyam', 'hari', 'krish', 'john', 'shyam'}

# student = ['ram', 'ktm', 'ram@email.com', 98123456780]

# student_dict = {'name': 'ram', 'address': 'ktm', 
#         'email': 'ram@email.com', 'mobile': 98123456780}

# for i in student_dict:
#     print(i, ': ', student_dict[i])



# days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 
#         'Thursday', 'Friday', 'Saturday']

# num = int(input('Enter a number'))

# if num<8 and num>0:
#     print(days[num-1])
# else:
#     print('Invalid')



# numbers = [10, 15, 7, 30, 20, 3, 12]

# max = numbers[0]
# min = numbers[0]

# for i in numbers:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print(max,',', min)

# students1 = [
#     ['ram', 'ktm', 'ram@email.com', 98123456780],
#     ['shyam', 'lalitpur', 'shyam@email.com', 98123456780],
#     ['hari', 'ilam', 'hari@email.com', 98123456780],
#     ['krishna', 'butwal', 'krish@email.com', 98123456780],
# ]

# students2 = (
#     ['ram', 'ktm', 'ram@email.com', 98123456780],
#     ['shyam', 'lalitpur', 'shyam@email.com', 98123456780],
#     ['hari', 'ilam', 'hari@email.com', 98123456780],
#     ['krishna', 'butwal', 'krish@email.com', 98123456780],
# )

# students3 = [
#     ('ram', 'ktm', 'ram@email.com', 98123456780),
#     ('shyam', 'lalitpur', 'shyam@email.com', 98123456780),
#     ('hari', 'ilam', 'hari@email.com', 98123456780),
#     ('krishna', 'butwal', 'krish@email.com', 98123456780),
# ]

# students4 = (
#     ('ram', 'ktm', 'ram@email.com', 98123456780),
#     ('shyam', 'lalitpur', 'shyam@email.com', 98123456780),
#     ('hari', 'ilam', 'hari@email.com', 98123456780),
#     ('krishna', 'butwal', 'krish@email.com', 98123456780),
# )

# students5 = [
#     {'name': 'ram', 'address': 'ktm', 'email': 'ram@email.com', 'mobile': 98123456780},
#     {'name': 'shyam', 'address': 'lalitpur', 'email': 'shyam@email.com', 'mobile': 98123456780},
#     {'name': 'hari', 'address': 'ilam', 'email': 'hari@email.com', 'mobile': 98123456780},
#     {'name': 'krishna', 'address': 'butwal', 'email': 'krish@email.com', 'mobile': 98123456780}
# ]

# students6 = {
#     'name': ['ram', 'shyam', 'hari', 'krishna'],
#     'address': ['ktm', 'lalitpur', 'ilam', 'butwal'],
#     'email': ['ram@email.com', 'ram@email.com', 'ram@email.com', 'ram@email.com'],
#     'mobile': [98123456780,98123456780,98123456780,98123456780]
# }

# students5[1]['address']
# students6['address'][1]

users = [
    {'name': 'ram', 'username': 'ram123', 'password': '12345', 'balance': 50000.00},
    {'name': 'hari', 'username': 'harry', 'password': '54321', 'balance': 120000.00},
    {'name': 'shyam', 'username': 'sam', 'password': '11111', 'balance': 80000.00},
    {'name': 'krishna', 'username': 'krish', 'password': '22222', 'balance': 300000.00}
]


def transaction():
    choice = input('Enter w for withdrawal / d for deposite')
    amount = float(input('Enter amount'))

    if choice == 'd':
        user['balance'] = user['balance']+amount
    elif choice == 'w':
        user['balance'] = user['balance']-amount
    else:
        print('Invalid selection')

    print('Your balance is NRs. ', user['balance'])
    transaction()


un = input('Enter username')
pw = input('Enter password')

for user in users:
    if user['username']==un and user['password']==pw:
        print('Welcome ', user['name'], '! Your balance is NRs. ', user['balance'])
        transaction()
        break
else:
    print('Wrong username or password')
