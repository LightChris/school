import json
import os

DIR = '/home/chris/PycharmProjects/school/'

students_data = json.load(open(os.path.join(DIR, 'Students.json'), 'r'))


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


def get_index_class(data, cl):
    for people in data:
        if cl == people['class']:
            return data.index(people)


for el in students_data:
    i = get_index_class(students_data, '6 А')
    if i == None:
        break
    students_data.pop(i)

save(students_data, 'Students_new.json')
