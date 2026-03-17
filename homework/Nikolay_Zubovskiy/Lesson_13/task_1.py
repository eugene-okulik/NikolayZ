# Нужно прочитать файлик, который лежит в репозитории в моей папке. Здесь: homework/eugene_okulik/hw_13/data.txt
#
# Файлик не копируйте и никуда не переносите. Напишите программу, которая читает этот файл,
# находит в нём даты и делает с этими датами то, что после них написано.
# Опирайтесь на то, что структура каждой строки одинакова:
# сначала идет номер, потом дата, потом дефис и после него текст.
# У вас должен получиться код,
# который находит даты и для даты под номером один в коде должно быть реализовано то действие,
# которое написано в файле после этой даты. Ну и так далее для каждой даты.

import os
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
file_path = os.path.dirname(os.path.dirname(base_path))
eo_file_path = os.path.join(file_path, 'eugene_okulik', 'hw_13',  'data.txt')
print(eo_file_path)


def read_file():
    with open(eo_file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line.rstrip('\n')


for line in read_file():
    print(line)
    parts = line.split(" - ")
    date_part = parts[0].split(". ")[1]
    date_obj = datetime.strptime(date_part, "%Y-%m-%d %H:%M:%S.%f")
    if line.startswith("1."):
        week_later = date_obj + timedelta(weeks=1)
        print(f'Дата на неделю позже: {week_later}')
    elif line.startswith("2."):
        day_of_week = date_obj.strftime("%A")
        print(f'День недели: {day_of_week}')
    elif line.startswith("3."):
        now = datetime.now()
        print(f'Сегодня: {now}')
        days_ago = (datetime.now() - date_obj).days
        print(f'Дней назад: {days_ago}')
