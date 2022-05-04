#variables
# name = 'Ram Kumar'
# age = 25 
# salary = 50000.0 
# is_married = False

# a = int(input('Enter a number'))
# b = int(input('Enter 2nd number'))

# a = 10
# b = 20
# if a > b:
#     print('A is greater than B')
# elif b > a:
#     print('B is greater than A')
# else:
#     print('A and B are equal')




# # Print Day according to user given number
# num = input('Enter a number')
# if num == '1':
#     print('Sunday')
# elif num == '2':
#     print('Monday')
# elif num == '3':
#     print('Tuesday')
# elif num == '4':
#     print('Wednesday')   
# elif num == '5':
#     print('thursday')  
# elif num == '6':
#     print('Friday')  
# elif num == '7':
#     print('Saturday')  
# else:
#     print('Invalid')




#Check if a user given number id odd or even.
# num = int(input('Enter a number'))

# if num%2 == 0:
#     print('Even')
# else:
#     print('Odd')





#Print multiplication of a number up to 10
# num = 5

# for i in range(1, 11):
#     # print(num, '*', i, '=', i*num)
#     print(f'{num} * {i} = {i*num}')

# j = 1
# while j <= 10:
#     print(j*num) 
#     j += 1

# 5*1 = 5
# 5*2 = 10

#Check if a user given number id prime or composite.
# num = int(input('Enter a number'))

# if num == 4:
#     print('composite')

# for i in range(2, num//2):
#     if num%i == 0:
#         print('Composite')
#         break
# else:
#     print('Prime')




# find factorial of a user given number.
# 5! = 5*4*3*2*1 = 1*2*3*4*5
# num = int(input('Enter a number'))
# fact = 1 
# for i in range(num, 0, -1):
#     fact = fact*i
# print(fact)


# print any 10 elements of fibonacci series
# 0 1 1 2 3 5 8 13 .....



'''
1*1=1   1*2=2   1*3=3 ..... 1*10=10
...............
10*1=10  10*2=20 .......... 10*10=100


for i in range(1, 11):
    for j in range(1, 11):
        # print(i, 'x', j, '=', i*j)
        print(f'{i} x {j} = {i*j}', end=' ')
    print()
'''

'''
*        1         1         54321    54321     12345   55555
**       12        22        5432     4321      1234    4444
***      123       333       543      321       123     333
****     1234      4444      54       21        12      22
*****    12345     55555     5        1         1       1
'''

# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*', end='')
#     print()


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end='')
#     print()


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i, end='')
#     print()


# for i in range(1, 6):
#     for j in range(5, i-1, -1):
#         print(j, end='')
#     print()

'''
*#*#*#
#*#*#*
*#*#*#
#*#*#*
*#*#*#
#*#*#*
'''
# for i in range(6):
#     for j in range(6):
#         if (i+j)%2 == 0:
#             print('*', end='')
#         else:
#             print('#', end='')
#     print()


# print factors of a given number
# 20:  1,2,4,5,10,20

#print multiples of a user given number upto user given boundary
# num= 3  bound = 20 output: 3, 6, 9, 12, 15, 18

# num = 3
# b = 20

# for i in range(1, b+1):
#     if num*i <= 20:
#         print(num*i)
#     else:
#         break

# i = 1
# while num*i < b:
#     print(num*i)
#     i += 1


name = '235234523'
city = 'kathmandu'
a = ['a',  'e', 'i', 'o', 'u']
print(city.index('u'))