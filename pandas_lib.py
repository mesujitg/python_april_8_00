import pandas

students_list = ['ram', 'shyam', 'hari', 'krish', 'john', 'shyam']

student_dict = {'name': 'ram', 'address': 'ktm', 'email': 'ram@email.com',
                'mobile': 98123456780}

# data = pandas.Series(student_dict)
# print(data)

students4 = (
    ('ram', 'ktm', 'ram@email.com', 98123456780),
    ('shyam', 'lalitpur', 'shyam@email.com', 98123456780),
    ('hari', 'ilam', 'hari@email.com', 98123456780),
    ('krishna', 'butwal', 'krish@email.com', 98123456780),
)

students5 = [
    {'name': 'ram', 'address': 'ktm', 'email': 'ram@email.com', 'mobile': 98123456780},
    {'name': 'shyam', 'address': 'lalitpur', 'email': 'shyam@email.com', 'mobile': 98123456780},
    {'name': 'hari', 'address': 'ilam', 'email': 'hari@email.com', 'mobile': 98123456780},
    {'name': 'krishna', 'address': 'butwal', 'email': 'krish@email.com', 'mobile': 98123456780}
]

students6 = {
    'name': ['ram', 'shyam', 'hari', 'krishna'],
    'address': ['ktm', 'lalitpur', 'ilam', 'butwal'],
    'email': ['ram@email.com', 'ram@email.com', 'ram@email.com', 'ram@email.com'],
    'mobile': [98123456780, 98123456780, 98123456780, 98123456780]
}

data = pandas.DataFrame(students6)
print(data)

# print(pandas.read_json('users.json'))
print(pandas.read_csv('users.csv'))
