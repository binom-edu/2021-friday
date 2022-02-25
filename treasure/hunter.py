import math, random

# Определяем константы
FIELD_WIDTH = 50    # ширина поля
FIELD_HEIGHT = 15   # высота поля
MAX_CHESTS = 3      # количество сундуков
MAX_ATTEMPTS = 20   # количество попыток

# создаем новую карту
def getNewMap() -> list:
    abc = '~`'
    result = []
    for i in range(FIELD_HEIGHT):
        buf = [random.choice(abc) for j in range(FIELD_WIDTH)]
        result.append(buf)
    return result

# выводим карту
def printMap(field: list):
    # выводим заголовки
    print('  |', end='')
    for i in range(FIELD_WIDTH):
        print(i // 10, end='')
    print()
    print('  |', end='')
    for i in range(FIELD_WIDTH):
        print(i % 10, end='')
    print()
    print('-' * (FIELD_WIDTH + 6))
    
    for i in range(FIELD_HEIGHT):
        # for j in i:
        #     print(j, end='')
        # print()
        print("%2d" % i, '|', ''.join(field[i]), '|', i, sep='')
    print('-' * (FIELD_WIDTH + 6))
    print('  |', end='')
    for i in range(FIELD_WIDTH):
        print(i // 10, end='')
    print()
    print('  |', end='')
    for i in range(FIELD_WIDTH):
        print(i % 10, end='')
    print()

# создаем сундуки с сокровищами
def hideChests() -> list:
    chests = []
    i = 0
    while i < MAX_CHESTS:
        y = random.randint(0, FIELD_HEIGHT - 1)
        x = random.randint(0, FIELD_WIDTH - 1)
        if not (y, x) in chests: # убеждаемся, что такого сундука еще нет
            chests.append((y,x))
            i += 1
    return chests

# определяем расстояние между двумя точками
def distance(a: tuple, b: tuple) -> int:
    return round(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5)

# ищем ближайший сундук
def radar(chests: list, coords: tuple) -> int:
    ans = 10
    for chest in chests:
        ans = min(distance(chest, coords), ans)
    return ans

# получаем ход пользователя
def getUserMove() -> tuple:
    pass

t = getNewMap()
printMap(t)
chests = hideChests()
print(chests)