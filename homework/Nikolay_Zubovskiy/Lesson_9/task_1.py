# Дана такая дата: "Jan 15, 2023 - 12:05:33"
# Преобразуйте эту дату в питоновский формат, после этого:
# 1. Распечатайте полное название месяца из этой даты
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"

import datetime

current_date = 'Jan 15, 2023 - 12:05:33'
current_date_format = datetime.datetime.strptime(current_date, '%b %d, %Y - %H:%M:%S')

print(current_date_format)
print(current_date_format.strftime('%B'))
print(current_date_format.strftime('%d.%m.%Y, %H:%M'))
