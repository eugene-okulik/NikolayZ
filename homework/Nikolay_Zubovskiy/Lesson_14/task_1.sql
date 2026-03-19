--
--INSERT INTO `groups` (title, start_date, end_date)
--VALUES ('ZZTop', 'jan 2026', 'jun 2026')
--
---- SELECT * FROM `groups` where title = 'ZZTop'
--
--INSERT INTO students (name, second_name, group_id)
--VALUES ('Fedor', 'Arhangelskiy', 22107)
--
---- SELECT  * from students s where group_id = 22107  (s.id = 22423)
--
--INSERT INTO books (title, taken_by_student_id)
--VALUES ('Гарри Потер и пираты Карибского моря', 22423),
--       ('Гарри Потер и дымовые завесы', 22423),
--       ('Гарри Потер и палеонтологические исследования', 22423)
--
--
--INSERT INTO subjects (title)
--VALUES ('Высшая философия огня'),
--       ('Психология дискретного материализма')
--
---- SELECT * FROM subjects s where title in('Высшая философия огня', 'Психология дискретного материализма') s.id = 14111, s.id = 14112
--
-- INSERT INTO lessons (title, subject_id)
-- VALUES ('Виды и типы огня', 14111),
--        ('Погружение в огонь', 14111),
--        ('Основы и вход в материализм', 14112),
--        ('Методы и практика материализма', 14112)
--
---- SELECT * FROM lessons l where subject_id in(14111, 14112) l.id = 75371, 75372, 75373, 75374
--
-- INSERT INTO marks (value, lesson_id, student_id)
-- VALUES ('отлично', 75371, 22423),
--        ('хорошо', 75372, 22423),
--        ('удовлетворительно', 75373, 22423),
--        ('хорошо', 75374, 22423)
--
-- SELECT * FROM marks m where student_id = 22423
--
-- SELECT * from books where taken_by_student_id = 22423
--
-- SELECT
-- 	s.id as student_id,
--    s.name as student_name,
--    s.second_name as student_second_name,
--    g.id as grp_id,
--    g.title as grp_name,
--    b.title as book_title,
--    m.value as mark_student,
--    l.title as lesson_title,
--    sub.title as subject_name
-- FROM students s
-- JOIN `groups` g on s.group_id = g.id
-- JOIN books b on s.id = b.taken_by_student_id
-- JOIN marks m on s.id = m.student_id
-- JOIN lessons l on m.lesson_id = l.id
-- JOIN subjects sub on l.subject_id = sub.id
-- WHERE s.id = 22423
-- ORDER BY sub.title
--
-- UPDATE marks SET value = 'наивысшый возможный балл' where lesson_id = 75372

INSERT INTO students (name, second_name, group_id)
VALUES ('Illarion', 'Bakardi', null)

INSERT INTO books (title, taken_by_student_id)
VALUES ('Гарри Поттер и шахматы бессмертных', 22424),
       ('Гарри Поттер и тайна Бермудского треугольника', 22424),
       ('Гарри Поттер и лабиринт Минотавра', 22424)

INSERT INTO `groups` (title, start_date, end_date)
VALUES ('AC/DC', 'jan 2026', 'jun 2026')

UPDATE students SET group_id = 22108 where id = 22424

INSERT INTO subjects (title)
VALUES ('Высшая философия огня'),
       ('Психология дискретного материализма')

 INSERT INTO lessons (title, subject_id)
 VALUES ('Виды и типы огня', 14111),
        ('Погружение в огонь', 14111),
        ('Основы и вход в материализм', 14112),
        ('Методы и практика материализма', 14112)

 INSERT INTO marks (value, lesson_id, student_id)
 VALUES ('отлично', 75371, 22424),
        ('удовлетворительно', 75372, 22424),
        ('удовлетворительно', 75373, 22424),
        ('отлично', 75374, 22424)

 SELECT * FROM marks m where student_id = 22424

 SELECT * from books where taken_by_student_id = 22424

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
 WHERE s.id = 22424
 ORDER BY sub.title
