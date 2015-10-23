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


# def get_index_class(data, name):
#     for cl in data[get_index(data, name)]:

teacher_full_name = "Черный Александр Сергеевич"
delete_class = '7 В'

with open('Teachers_id.json', 'r') as teach:
    teachers_data = json.load(teach)

    teachers_data[get_index(teachers_data, teacher_full_name)]['class'].remove(delete_class)
    save(teachers_data, 'Teachers_new.json')
    pass
