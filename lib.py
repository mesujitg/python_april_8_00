# import math
from math import *
import datetime as d
import re
from random import shuffle

# country_list = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua &amp; Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia &amp; Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany"]
# index = 0

# def show_word():
#     global index
#     word = country_list[index].upper()
#     wl = list(word)
#     shuffle(wl)
#     for i in wl:
#         print(i, end='')
#     print()
#     ans = input('Enter correct word: ')

#     if ans.lower() == word.lower():
#         print('correct')
#         if index == len(country_list) - 1:
#             print('All levels are completed')
#         else:    
#             index += 1
#             show_word()
#     else:
#         print('incorrect')
#         show_word()

# show_word()

# a = ['ram', 'shyam', 'hari', 'krishna']
# print(a)
# shuffle(a)
# print(a)

# print(sqrt(25))
# print(math.ceil(5.99999))
# print(math.floor(5.99999))
# print(math.factorial(5))
# print(pi)

# print(d.datetime.now())

# email = input('Enter your email')
# regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# mobile = input('Enter your mobile')
# regex_mobile = r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}'

# if not re.fullmatch(regex_email, email):
#     print('invalid email')
# elif not re.fullmatch(regex_mobile, mobile):
#     print('invalid mobile')
# else:
#     print('ok')

'''
create a function which asks for name, email, mobile, username and 
password and appends it to a users list. Use suitable validations.
'''
users = []

def validate(name, email, phone):
    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    regex_mobile = r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}'
    err_msg = ''
    if not name.isalpha():
        err_msg += 'Invalid Name \n'
    if not re.fullmatch(regex_email, email):
        err_msg += 'Invalid Email \n'
    if not re.fullmatch(regex_mobile, phone):
        err_msg += 'Invalid Phone \n'
    
    return err_msg


def register():
    name = input('Enter your Name: ')
    email = input('Enter your Email: ')
    phone = input('Enter your Phone: ')
    if validate(name, email, phone) == '':
        users.append({'Name': name, 'Email': email, 'Phone':phone})
        print(users)
    else:
        print(validate(name, email, phone))
        register()


# def check(name):
#     while not name.isalpha():
#         name = input('Enter Name')
#     else:
#         print(name)

# name = input('Enter name')
# check(name)
