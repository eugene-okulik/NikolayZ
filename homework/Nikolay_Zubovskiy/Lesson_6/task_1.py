
# формат-коды для подчеркиваия текста, текст между будет подчеркнут(источник чат gpt)
UNDER = '\033[4m'
RESET = '\033[0m'

ING = UNDER + 'ING' + RESET
text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
text_list = text.split()
text_list_new = []

for word in text_list:
    # if word[-1] == ',' or word[-1] == '.':
    # if word.endswith(',') or word.endswith('.'):
    if word[-1] in '(,.)':
        # word = '{0}{1}{2}'.format(word[:-1], _ing, word[-1])
        # word = word[:-1] + ING + word[-1]
        word = f"{word[:-1]}{ING}{word[-1]}"
    else:
        # word = word + ING
        word = f'{word}{ING}'
    text_list_new.append(word)

text_new = ' '.join(text_list_new)
print(f'"{text_new}"')
