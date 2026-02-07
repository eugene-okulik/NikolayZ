
results = ('результат операции: 42', 'результат операции: 54', 'результат работы программы: 209', 'результат: 2')
ADD_VALUE = 10


def result_int(text):
    index = text.index(':')
    return int(text[index + 1:]) + ADD_VALUE


for text in results:
    print(result_int(text))
