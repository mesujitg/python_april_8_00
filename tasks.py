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
prediction_1 = {'ram':[1,1], 'shyam':[0,1], 'hari':[2,1], 'gopal':[1,2]}
prediction_2 = [[1,1], [0,1], [2,1], [1,2]]