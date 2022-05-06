# Calculate percentage of given students. 
# Also print the subjects of equal marks
marks_ram = {'English': 75, 'Nepali': 65, 'Maths': 85, 'Science': 78, 
                'Social': 55}
marks_shyam = {'English': 73, 'Nepali': 70, 'Maths': 85, 'Science': 81, 
                'Social': 55}

sum_ram = 0
sum_shyam = 0

for i in marks_ram:
    sum_ram += marks_ram[i]
    sum_shyam += marks_shyam[i]
    if marks_ram[i]==marks_shyam[i]:
        print(i, ":", marks_ram[i])

print("Ram:", (sum_ram/5))
print("Shyam:", (sum_shyam/5))


'''
fixture   prediction   result
-------  -----------   -------
A        1, 0, 2, 1       0
B        1, 1, 1, 2       1

C       
D

E
F
'''
# prediction_1 = {'ram':[1,1], 'shyam':[0,1], 'hari':[2,1], 'gopal':[1,2]}
# prediction_2 = [[1,1], [0,1], [2,1], [1,2]]

# import random

# def bingo(set):
#     set1 = ''.join(random.sample(set, 3))
#     set2 = ''.join(random.sample(set, 3))
#     set3 = ''.join(random.sample(set, 3))

#     num = input('Enter your Number')

#     if num in set1 and num in set2 and num in set3:
#         print('Bingo')
#         bingo('123456')
#     else:
#         count = 0
#         if num in set1:
#             count += 1
#         if num in set2:
#             count += 1
#         if num in set3:
#             count += 1
#         print('Your missed by:', 3-count)
#         bingo('123456')

# bingo('123456')




# create a MCQ console app 
qns = [
    'What is area of Nepal',
    'Who is first prime minister of Nepal',
    'Height of Mt. Everest is',
    'qn4',
    'qn5',
]

ans = [
    '147181 sq km',
    'Bhimsen Thapa',
    '8848.8 m',
    'ans4',
    'ans5',
]

options = [
    ['147818 sq km', '157818 sq km', '157181 sq km', '147181 sq km'], 
    ['Bhimsen Thapa', 'BP Koirala', 'Kalu Pande', 'Jang B Rana'], 
    ['8848 m', '8848.4 m', '8884.8 m', '8848.8 m'], 
    ['a', 'b', 'c', 'd'], 
    ['a', 'b', 'c', 'd']
]

user_answer = []

q_no = 0

print(q_no+1, '. ', qns[q_no])
for op in options[q_no]:
    print(op)

user_choice = input('Enter a or b or c or d')

