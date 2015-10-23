import json
import os

DIR = '/home/chris/PycharmProjects/school/'


def save(data, file_name):
    """
    Сохраняем данные(data) в файл с именем file_name в формате JSON
    :param data: сохраняемые данные
    :type data: any type
    :param file_name: имя файла
    :type file_name: str
    """
    file = open(os.path.join(DIR, file_name), 'w', encoding="UTF-8")
    file.write(json.dumps(data, ensure_ascii=False))
    file.close()


def get_index(data, full_name):
    for people in data:
        if full_name == people['surname'] + ' ' + people['name'] + ' ' + people["middle_name"]:
            return data.index(people)


with open('Students_id.json', 'r') as stud:
    students_data = json.load(stud)

    student_full_name = "Иванов Иван Игоревич"  # Ф.И.О.
    students_data.pop(get_index(students_data, student_full_name))
    save(students_data, 'Students_new.json')
    pass
