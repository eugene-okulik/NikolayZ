# Задание

# В папке /homework/eugene_okulik/Lesson_16/hw_data лежит csv файл.
# Файл никуда не копируйте и не переносите.
# Прочитайте этот файл с помощью модуля csv и проверьте есть ли те данные,
# которые там перечислены, в нашей базе данных.
# При подключении к базе данных не прописывайте данные подключения в коде,
# а воспользуйтесь подходом .env c такими переменными:
# DB_USER, DB_PASSW, DB_HOST, DB_PORT, DB_NAME.
# Я на своем компе уже создал файл .env с этими переменными, так что,
# если все сделаем одинаковые названия, будет работать всё универсально
# В результате сравнения, если обнаружится, что каких-то данных,
# которые есть в файле, нет в базе данных, распечатайте каких данных не хватает в базе.
# Подсказка для самопроверки: в базе нет данных, которые полностью соответствуют первой строке файла,
# но в базе есть данные, которые соответствуют второй строке файла.

import dotenv
import os
import csv
import mysql.connector as mysql

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSWD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_DATABASE')
)

with (open('/Users/purrweb/PycharmProjects/NikolayZ/homework/eugene_okulik/Lesson_16/hw_data/data.csv', newline='')
      as csv_file):
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

cursor = db.cursor(dictionary=True)

query = '''
SELECT s.id
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects sub ON l.subject_id = sub.id
WHERE s.name = %s
  AND s.second_name = %s
  AND g.title = %s
  AND b.title = %s
  AND sub.title = %s
  AND l.title = %s
  AND m.value = %s
'''
missing_data = []

for row in data:
    value = (
        row['name'],
        row['second_name'],
        row['group_title'],
        row['book_title'],
        row['subject_title'],
        row['lesson_title'],
        row['mark_value']
    )
    cursor.execute(query, value)
    result = cursor.fetchall()
    if not result:
        missing_data.append(row)
    else:
        for i in range(len(result)):
            result_id = result[i]['id']
            print(f"ID студента с данными: {row['name']}-{row['second_name']}-{row['group_title']}-"
                  f"{row['book_title']}-{row['subject_title']}-{row['lesson_title']}-"
                  f"{row['mark_value']} = {result_id}")

print('В БД нет данных по следующим студентам:')
for row in missing_data:
    print(f"{row['name']}-{row['second_name']}-{row['group_title']}-{row['book_title']}-"
          f"{row['subject_title']}-{row['lesson_title']}-{row['mark_value']}")

db.close()
