my_dict = {'tuple': ("Иван", "Иванов", "30", "инженер", "85000.00"),
           'list': ["яблоко", "банан", "мандарин", "апельсин", "виноград"],
           'dict': {"title": "Преступление и наказание",
                    "author": "Достоевский Ф.М.",
                    "year": 1866,
                    "genre": "роман",
                    "language": "русский"
                    },
           'set': {"Python", "JavaScript", "Java", "C++", "Go"}
           }
print(my_dict['tuple'][-1])

my_dict['list'].append('гранат')
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = 'New element'
my_dict['dict'].pop('language')

my_dict['set'].add('Pascal')
my_dict['set'].pop()

print(my_dict)




