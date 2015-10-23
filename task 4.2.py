import json

DIR = '/home/chris/PycharmProjects/school/'

id_list = []
surname = "Кузин"
with open('Students_id.json', 'r') as stud:
    students_data = json.load(stud)

    for student in students_data:
        if surname == student['surname']:
            i = student['id']
            id_list.append(i)

    for student in students_data:
        for el in id_list:
            if el == student['id']:
                print(student['name'] + ' ' + student['middle_name'] + ' ' + student['surname'])
    pass
