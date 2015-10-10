import json
import os

DIR = '/home/chris/PycharmProjects/school/'

teachers_data = json.load(open(os.path.join(DIR, 'Teachers.json'), 'r'))


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


teacher_full_name = "Черный Александр Сергеевич"  # Ф.И.О.
teachers_data.pop(get_index(teachers_data, teacher_full_name))
save(teachers_data, 'Teachers_new.json')
