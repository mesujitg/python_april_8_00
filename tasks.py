# Calculate percentage of given students. 
# Also print the subjects of equal marks
# marks_ram = {'English': 75, 'Nepali': 65, 'Maths': 85, 'Science': 78, 
#                 'Social': 55}
# marks_shyam = {'English': 73, 'Nepali': 70, 'Maths': 85, 'Science': 81, 
#                 'Social': 55}

# sum_ram = 0
# sum_shyam = 0

# for i in marks_ram:
#     sum_ram += marks_ram[i]
#     sum_shyam += marks_shyam[i]
#     if marks_ram[i]==marks_shyam[i]:
#         print(i, ":", marks_ram[i])

# print("Ram:", (sum_ram/5))
# print("Shyam:", (sum_shyam/5))


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
#         print('Bingo', set1, set2, set3)
#         bingo('123456')
#     else:
#         count = 0
#         if num in set1:
#             count += 1
#         if num in set2:
#             count += 1
#         if num in set3:
#             count += 1
#         print('Patterns:', set1, set2, set3)
#         bingo('123456')

# bingo('123456')




# create a MCQ console app 
questions = [
    'What is area of Nepal?',
    'Who is first prime minister of Nepal?',
    'Height of Mt. Everest is:',
    'Population of Nepal is: ',
    'No of National Parks in Nepal: ',
]

answers = [
    '147181 sq km',
    'Bhimsen Thapa',
    '8848.8 m',
    '29,140,000',
    '9',
]

# options = [
#     {'a':'147818 sq km', 'b':'157818 sq km', 'c':'157181 sq km', 'd':'147181 sq km'}, 
#     {'a':'Bhimsen Thapa', 'b':'BP Koirala', 'c':'Kalu Pande', 'd':'Jang B Rana'}, 
#     {'a':'8848 m', 'b':'8848.4 m', 'c':'8884.8 m', 'd':'8848.8 m'}, 
#     {'a':'39,140,000', 'b':'19,140,000', 'c':'29,140,000', 'd':'49,140,000'}, 
#     {'a':'6', 'b':'7', 'c':'8', 'd':'9'}
# ]

options = [
    ['147818 sq km', '157818 sq km', '157181 sq km', '147181 sq km'], 
    ['Bhimsen Thapa', 'BP Koirala', 'Kalu Pande', 'Jang B Rana'], 
    ['8848 m', '8848.4 m', '8884.8 m', '8848.8 m'], 
    ['39,140,000', '19,140,000', '29,140,000', '49,140,000'], 
    ['6', '7', '8', '9']
]

choices = {'a':0, 'b':1, 'c':2, 'd':3}

#ans = b 
# options[q_no][choices[ans]]

q_no = 0
score = 0

def show_qn_option():
    global q_no, score
    print(f'{q_no+1}. {questions[q_no]}')
    # for op in options[q_no]:
    #     print(f'{op}) {options[q_no][op]}')
    print('a)', options[q_no][0])
    print('b)',options[q_no][1])
    print('c)',options[q_no][2])
    print('d)',options[q_no][3])
    ans = input('Enter a/b/c/d: ')

    # check if ans is correct or not and do score = score+1 if correct
    # if answers[q_no] == options[q_no][ans]:
    #     score += 1
    if answers[q_no] == options[q_no][choices[ans]]:
        score += 1
    
    if q_no < len(questions)-1:
        q_no += 1
        show_qn_option()
    else:
        print('You have comleted the test. Your score is: ', score)

show_qn_option()
