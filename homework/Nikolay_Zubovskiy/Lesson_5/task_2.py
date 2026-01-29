response_str_1 = 'результат операции: 42'
response_str_2 = 'результат операции: 514'
response_str_3 = 'результат работы программы: 9'

response_int_1 = int(response_str_1[-2:]) + 10
response_int_2 = int(response_str_2[-3:]) + 10
response_int_3 = int(response_str_3[-1:]) + 10
print('Вариант через срезы:', response_int_1, response_int_2, response_int_3, sep='\n')

response_int_1 = int(response_str_1.split()[-1]) + 10
response_int_2 = int(response_str_2.split()[-1]) + 10
response_int_3 = int(response_str_3.split()[-1]) + 10
print('Вариант через сплит:', response_int_1, response_int_2, response_int_3, sep='\n')