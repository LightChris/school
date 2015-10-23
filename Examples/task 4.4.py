import json

DIR = '/home/chris/PycharmProjects/school/'

teach_class = '6 Б'
id_list = []
with open('Teachers_id.json', 'r') as teach:
    teachers_data = json.load(teach)

    for teacher in teachers_data:
        if teach_class in teacher['class']:
            id_list.append(teacher['id'])

    print(id_list)
    pass
