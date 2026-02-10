import sys
sys.set_int_max_str_digits(30000) # чтобы не было ошибки с переполнением при выводе длинного числа

def fibo_generate(number = 100):
    a, b = 0, 1
    for _ in range(number):
        yield a
        a, b = b, a + b


# пятое число, двухсотое число, тысячное число, стотысячное число
count = 1
for number in fibo_generate(100001):
    if count == 5:
        print(number)
    elif count == 200:
        print(number)
    elif count == 1000:
        print(number)
    elif count == 100000:
        print(number)
    count += 1
