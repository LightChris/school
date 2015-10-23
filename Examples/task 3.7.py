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


def get_index_school(data, school):
    for people in data:
        if school == people['school']:
            return data.index(people)


teacher_school = '67 школа'

with open('Teachers_id.json', 'r') as teach:
    teachers_data = json.load(teach)
    for el in teachers_data:
        i = get_index_school(teachers_data, teacher_school)
        if i == None:
            break
        teachers_data.pop(i)

    save(teachers_data, 'Teachers_new.json')
    pass
