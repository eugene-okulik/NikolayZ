import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    database='st-onl'
)


class Student:
    def __init__(self, name, second_name, group_id):
        self.name = name
        self.second_name = second_name
        self.group_id = group_id


class Book:
    def __init__(self, title, taken_by_student_id):
        self.title = title
        self.taken_by_student_id = taken_by_student_id


class Group:
    def __init__(self, title, start_date, end_date):
        self.title = title
        self.start_date = start_date
        self.end_date = end_date


class Subject:
    def __init__(self, title):
        self.title = title


class Lesson:
    def __init__(self, title, subject_id):
        self.title = title
        self.subject_id = subject_id

    def get_lesson_id(self, cursor):
        query = "SELECT id FROM lessons WHERE title = %s"
        cursor.execute(query, (self.title,))
        lesson_id = cursor.fetchone()['id']
        return lesson_id


student_1 = Student('Violetta', 'Grineva', None)
book_1 = Book('Гарри Поттер и морские глубины', None)
book_2 = Book('Гарри Поттер и космические пираты', None)
book_3 = Book('Гарри Поттер и таксисты', None)
group_1 = Group('NightWish', 'jan 2026', 'jun 2026')
subject_1 = Subject('Всемирная магия событий')

cursor = db.cursor(dictionary=True)

query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
cursor.execute(query, (student_1.name, student_1.second_name))

query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(query, (group_1.title, group_1.start_date, group_1.end_date))

query = "INSERT INTO subjects (title) VALUES (%s)"
cursor.execute(query, (subject_1.title,))

db.commit()

query = "SELECT id FROM students WHERE name = %s and second_name = %s"
cursor.execute(query, (student_1.name, student_1.second_name))
student_1_id = cursor.fetchone()['id']
print('id студента = ', student_1_id)

query = "SELECT id FROM `groups` WHERE title = %s"
cursor.execute(query, (group_1.title,))
group_1_id = cursor.fetchone()['id']
print('id группы = ', group_1_id)

query = "SELECT id FROM subjects WHERE title = %s"
cursor.execute(query, (subject_1.title,))
subject_1_id = cursor.fetchone()['id']
print('id предмета = ', subject_1_id)

lesson_1 = Lesson('Взаимодействие с магией', subject_1_id)
lesson_2 = Lesson('Движение в магической воронке событий', subject_1_id)

query = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(query, (group_1_id, student_1_id))

query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
value = [
    (book_1.title, student_1_id),
    (book_2.title, student_1_id),
    (book_3.title, student_1_id)
]
cursor.executemany(query, value)

query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
value = [
    (lesson_1.title, lesson_1.subject_id),
    (lesson_2.title, lesson_2.subject_id),
]
cursor.executemany(query, value)

db.commit()

# query = "SELECT id FROM lessons WHERE title = %s"
# cursor.execute(query, (lesson_1.title,))
# lesson_1_id = cursor.fetchone()['id']
lesson_1_id = lesson_1.get_lesson_id(cursor)
print('id урока_1 = ', lesson_1_id)
# query = "SELECT id FROM lessons WHERE title = %s"
# cursor.execute(query, (lesson_2.title,))
# lesson_2_id = cursor.fetchone()['id']
lesson_2_id = lesson_2.get_lesson_id(cursor)
print('id урока_2 = ', lesson_2_id)

query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
value = [
    ("удовлетворительно", lesson_1_id, student_1_id),
    ("неудовлетворительно", lesson_2_id, student_1_id)
]
cursor.executemany(query, value)

db.commit()

query = '''
SELECT
 	s.id as student_id,
    s.name as student_name,
    s.second_name as student_second_name,
    g.id as grp_id,
    g.title as grp_name,
    b.title as book_title,
    m.value as mark_student,
    l.title as lesson_title,
    sub.title as subject_name
 FROM students s
 JOIN `groups` g on s.group_id = g.id
 JOIN books b on s.id = b.taken_by_student_id
 JOIN marks m on s.id = m.student_id
 JOIN lessons l on m.lesson_id = l.id
 JOIN subjects sub on l.subject_id = sub.id
 WHERE s.id = %s
 ORDER BY sub.title'''
cursor.execute(query, (student_1_id,))
result = cursor.fetchall()
for i, data in enumerate(result, 1):
    print(f'{i}. {data}')

db.close()
