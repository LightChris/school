import json
import os

DIR = '/home/chris/PycharmProjects/school/'

teachers_data = json.load(open(os.path.join(DIR, 'Teachers_new.json'), 'r'))


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


def get_index(data, surname):
    for teacher in data:
        if surname == teacher['surname']:
            return data.index(teacher)


teacher_name = "Фрянова"
new_class = '9 В'

teachers_data.append(teachers_data[get_index(teachers_data, teacher_name)]['class'].append(new_class))
save(teachers_data, 'Teachers_new.json')