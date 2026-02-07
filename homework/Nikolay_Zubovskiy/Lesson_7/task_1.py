from colorama import Fore, init
init(autoreset=True)

colors = {
    'red': Fore.LIGHTRED_EX,
    'blue': Fore.LIGHTBLUE_EX,
    'yellow': Fore.LIGHTYELLOW_EX,
    'green': Fore.LIGHTGREEN_EX,
    'magenta': Fore.LIGHTMAGENTA_EX
}

def message(msg_type, num):
    if msg_type == 'input':
        return (f"Вы ввели {colors['green']}{num} - {colors['red']}это не верное число!")
    elif msg_type == 'bigger':
        return (f"Число {colors['green']}{num} - {colors['blue']}больше загаданного, попробуйте еще раз!")
    elif msg_type == 'smaller':
        return (f"Число {colors['green']}{num} - {colors['yellow']}меньше загаданного, попробуйте еще раз!")
    elif msg_type == 'success':
        return (f"{colors['magenta']}Поздравляем! \nВы ввели число {colors['green']}{num} - "
                f"{colors['magenta']}это верное число, вы победили!")

secret_num = 42

while True:
    input_num = int(input('Введите число: '))
    if input_num == secret_num:
        break
    print(message('input', input_num))
    if input_num > secret_num:
        print(message('bigger', input_num))
    else:
        print(message('smaller', input_num))

print(message('success', input_num))
