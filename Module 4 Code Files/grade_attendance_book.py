billy = {
    'name': 'Billy',
    'grades': [100, 80, 67, 100, 89],
    'attendance': [True, True, True, True, True]
}

sarah = {
    'name': 'Sarah',
    'grades': [0, 99, 0, 100, 0],
    'attendance': [True, False, True, False, True]
}

ben = {
    'name': 'Ben',
    'grades': [60, 82, 71, 92, 100],
    'attendance': [False, False, False, False, False]
}

students = {'1': billy, '2': sarah, '3': ben}

#get number of students
print(len(students)) #number of keys

#get all student ids
print(students.keys()) #gets all keys in dict

#iterate over students
for k in students:
    print('key:', k)

#get billy's attendance
billy = students['1']
print(billy['attendance'])

#get sarah's grades
sarah = students.get('2')
print(sarah.get('grades'))

#get all key:value pairs for ben
ben = students.get('3')
items = ben.items() #returns sequence of tuples
for key, val in items:
    print(key, val)

#get average student grade for all assignments
grades = []
items = students.items() #key:value pairs for students
for key, val in items:
    for g in val['grades']:
        grades.append(g)

#average grade
print(round(sum(grades) / len(grades)))

#another way to do this
grades_concatenated = []
items = students.items() #key:value pairs for students
for key, val in items:
    grades_concatenated += val['grades'] #concatenate list of grades

#average grade
print(round(sum(grades_concatenated) / len(grades_concatenated)))
