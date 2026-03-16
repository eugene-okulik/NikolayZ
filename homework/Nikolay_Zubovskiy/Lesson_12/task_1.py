# Задание
# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов.
# Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни) (и это тоже метод).

class Flowers:
    def __init__(self, name, fresh, color, length, price):
        self.name = name
        self.fresh = fresh
        self.color = color
        self.length = length
        self.price = price


class Tulip(Flowers):
    def __init__(self, name, fresh, color, length, price, petal):
        super().__init__(name, fresh, color, length, price)
        self.petal = petal


class Rose(Flowers):
    def __init__(self, name, fresh, color, length, price, has_thorn):
        super().__init__(name, fresh, color, length, price)
        self.has_thorn = has_thorn


class Lily(Flowers):
    def __init__(self, name, fresh, color, length, price, has_smell):
        super().__init__(name, fresh, color, length, price)
        self.has_smell = has_smell


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def time_to_die(self):
        time = 0
        for flower in self.flowers:
            time += flower.fresh
        return int(time / len(self.flowers))

    def sort_by_fresh(self):
        self.flowers.sort(key=lambda x: x.fresh, reverse=True)

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.color)

    def sort_by_length(self):
        self.flowers.sort(key=lambda x: x.length)

    def sort_by_price(self):
        self.flowers.sort(key=lambda x: x.price)

    def search_by_fresh(self, average_fresh):
        return [flower for flower in self.flowers if flower.fresh >= average_fresh]

    def search_by_color(self, color):
        return [flower for flower in self.flowers if flower.color == color]


tulip_1 = Tulip('Тюльпан 1', 10, 'белый', 20, 100, 5)
tulip_2 = Tulip('Тюльпан 2', 10, 'красный', 25, 150, 6)
tulip_3 = Tulip('Тюльпан 3', 10, 'желтый', 30, 200, 5)

rose_1 = Rose('Флоребунда', 15, 'белый', 30, 350, True)
rose_2 = Rose('Чайная', 10, 'красный', 25, 250, False)
rose_3 = Rose('Клумбовая', 30, 'розовый', 35, 500, True)

lily_1 = Lily('Лилии 1', 20, 'белый', 50, 600, True)
lily_2 = Lily('Лилии 2', 20, 'розовый', 55, 700, True)
lily_3 = Lily('Лилии 3', 20, 'красный', 60, 800, False)

bouquets = [
    Bouquet([rose_1]),
    Bouquet([tulip_1, tulip_2, rose_1]),
    Bouquet([tulip_1, rose_1, rose_2, lily_1, lily_2]),
    Bouquet([rose_1, rose_1, rose_1, rose_2, rose_3])
]

print('Время увядания букета 4:', bouquets[3].time_to_die(), 'дн')
print('Цена букета 2:', bouquets[2].total_price(), 'руб')

print("\nCвежесть цветов в букете 4:")
fresh_flowers = bouquets[3].search_by_fresh(15)
for flower in fresh_flowers:
    print(f"{flower.name}, свежесть: {flower.fresh} дн")

print('\nБелые цветы букета 2:')
color_flowers = bouquets[1].search_by_color('белый')
for flower in color_flowers:
    print(f"{flower.name}")
