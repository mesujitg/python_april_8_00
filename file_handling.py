import csv, json

# file = open('users.csv', 'r')
# file_w = open('users.csv', 'w')
# data = csv.reader(file)
# output = csv.writer('')


# users = []
# for d in data:
#     users.append(d)
# print(users)
file_json = open('users.json', 'r')
print(json.load(file_json))



# try:
#     file_r = open('users.txt', 'r') # file to read
#     file_w = open('users.txt', 'w') # file to write
#     file_a = open('users.txt', 'a') # file to write new data (append)
#     users = file_r.readlines()
#     output = ['hello there! \n', 'How are you? \n',
#               'Where are you from? \n']
#     file_w.writelines(output)
#     file_a.writelines(output)
# except Exception as e:
#     print(e)

