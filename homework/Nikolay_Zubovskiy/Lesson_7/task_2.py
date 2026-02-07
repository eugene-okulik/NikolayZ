words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def pr_1(value, count):
    while count != 0:
        print(value, end='')
        count -= 1
    print()


for value, count in words.items():
    if count == 0:
        break
    pr_1(value, count)
    # print(value*count) вариант без использования функции
