import json
import os

DIR = '/home/chris/PycharmProjects/school/'

with open('Students_id.json', 'r') as stud:
    with open('Teachers_id.json', 'r') as teach:
        students = json.load(stud)
        teachers = json.load(teach)
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
        print('\n\nЗадание 2.1\n')
        class_list = []
        teacher_full_name = 'Владимир Вышкин'
        for teacher in teachers:
            if teacher_full_name == '%s %s' % (teacher['name'], teacher['surname']):
                class_list = teacher['class']

        for el in class_list:
            for student in students:
                if student['class'] == el:
                    print(student['surname'], student['name'], student['middle_name'])

        # TODO: №2.2
        print('\n\nЗадание 2.2\n')
        student_full_name = 'Александр Красный'
        for student in students:
            if student['name'] + ' ' + student['surname'] == student_full_name:
                for teacher in teachers:
                    if student['school'] == teacher['school'] and student['class'] in teacher['class']:
                        print(teacher['name'] + ' ' + teacher['middle_name'] + ' ' + teacher['surname'])
                break
        pass
    pass
