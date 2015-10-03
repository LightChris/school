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


teachers_data = json.load(open(os.path.join(DIR, 'Teachers.json'), 'r'))

teacher = {
    "name": "Андрей",
    "middle_name": "Владимирович",
    "surname": "Титов",
    "school": "67 школа",
    "class": [
        "5 А",
        "6 Б",
        "7 В",
        "7 Г"
    ],
    "birth_day": "04.08.1978"
}

teacher2 = {
    "name": "Елена",
    "middle_name": "Викторовна",
    "surname": "Титова",
    "school": "67 школа",
    "class": [
        "6 Б",
        "7 В",
        "7 Г"
    ],
    "birth_day": "22.09.1978"
}

teacher3 = {
    "name": "Анастасия",
    "middle_name": "Михайловна",
    "surname": "Фрянова",
    "school": "12 гимназия",
    "class": [
        "6 А",
        "6 Б",
        "6 Г",
        "7 В"
    ],
    "birth_day": "04.08.1978"
}

teachers_data.append(teacher)
teachers_data.append(teacher2)
teachers_data.append(teacher3)

save(teachers_data, 'Teachers_new.json')
