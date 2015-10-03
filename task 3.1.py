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


students_data = json.load(open(os.path.join(DIR, 'Students.json'), 'r'))
# os.path.join - Вставляет нужный \ (Для исскуственного поддержания кросс-платформенности)
# константа - переменная которая не должна изменятся

student = {
    "name": "Петр",
    "middle_name": "Алексеевич",
    "surname": "Первый",
    "school": "67 школа",
    "class": "7 В",
    "birth_day": "06.06.1997"
}

student2 = {
    "name": "Евгений",
    "middle_name": "Александрович",
    "surname": "Кравчук",
    "school": "67 школа",
    "class": "7 Г",
    "birth_day": "23.11.1999"
}

student3 = {
    "name": "Лилия",
    "middle_name": "Романовна",
    "surname": "Чалая",
    "school": "67 школа",
    "class": "7 В",
    "birth_day": "19.08.1999"
}

student4 = {
    "name": "Виктория",
    "middle_name": "Александровна",
    "surname": "Ким",
    "school": "67 школа",
    "class": "7 Г",
    "birth_day": "12.08.1999"
}

student5 = {
    "name": "Денис",
    "middle_name": "Олегович",
    "surname": "Михайлов",
    "school": "12 гимназия",
    "class": "7 В",
    "birth_day": "66.66.6666"
}

students_data.append(student)
students_data.append(student2)
students_data.append(student3)
students_data.append(student4)
students_data.append(student5)

save(students_data, 'Students_new.json')

