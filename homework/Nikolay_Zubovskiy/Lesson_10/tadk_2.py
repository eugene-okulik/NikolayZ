# Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция
# Код, использующий этот декоратор может выглядеть, например, так:
#
# @repeat_me
# def example(text):
#     print(text)
#
# example('print me', count=2)

# В результате работы будет такое:
# print me
# print me

# Если есть время и желание погуглить и повозиться, то можно попробовать создать декоратор,
# который сможет обработать такой код:

# @repeat_me(count=2)
# def example(text):
#     print(text)
#
# example('print me')


def repeat_me_1(func):

    def wrapper(*args):
        count = args[1]
        for i in range(count):
            func(*args)

    return wrapper


@repeat_me_1
def example_1(text, count):
    print(text)


example_1('print me', 5)


def repeat_me_2(count):
    def decorator(func):
        def wrapper(*args):
            for i in range(count):
                func(*args)
        return wrapper
    return decorator


@repeat_me_2(3)
def example_2(text):
    print(text)


example_2('print mе, вложенный декоратор')
