import json

students = json.load(open('Students.json'))
teachers = json.load(open('Teachers.json'))

# TODO: №1.1
print('Задание 1.1\n')
for student in students:
    print('Ученик: ', student['name'])

# TODO: №1.2
print('\n\nЗадание 1.2\n')
for teacher in teachers:
    print('Учитель: ', teacher['name'])

# TODO: №1.3
cl = '6 А'
# cl = input('Введите класс ученика(пример: "5 A"): ')
print('\n\nЗадание 1.3\n')
for student in students:
    if student['class'] == cl:
        print(student['name'] + ' ' + student['surname'])

# TODO: №1.4
print('\n\nЗадание 1.4\n')
school = set()
for student in students:
    school.add(student['school'])
print('Все школы: ', school)

# TODO: №1.5
print('\n\nЗадание 1.5\n')
for student in students:
    surname = student['surname']
    i = 0
    for el in students:
        if el['surname'] == surname:
            i += 1
            if i == 2:
                print(student['name'], ' ', student['surname'])


# TODO: №2.1
# print('\n\nЗадание 2.1\n')
# teacher_students = []
# teacher_full_name = 'Александр Сергеевич Черный'
# for teacher in teachers:
#     teach = teacher['name'] + ' ' + teacher['middle_name'] + ' ' + teacher['surname']
#     if teacher_full_name == teach:
#         for student in students:
#             if student['school'] == teacher['school'] and student['class'] in teacher['class']:
#                 teacher_students.append('')