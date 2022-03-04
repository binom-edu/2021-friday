import math, random

# Определяем константы
FIELD_WIDTH = 50    # ширина поля
FIELD_HEIGHT = 15   # высота поля
MAX_CHESTS = 3      # количество сундуков
MAX_ATTEMPTS = 20   # количество попыток
abc = '~`'

# создаем новую карту
def getNewMap() -> list:
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
def getUserMove(field: list) -> tuple:
    while True:
        s = input('Укажите координаты (номер строки и столбца через пробел): ').split()
        if len(s) != 2:
            print('Требуется ввести два числа')
        elif not s[0].isdigit() or not s[1].isdigit():
            print('Требуется ввести два числа')
            continue
        x, y = int(s[1]), int(s[0])
        if not(0 <= x < FIELD_WIDTH and 0 <= y < FIELD_HEIGHT):
            print('Координаты должны быть в пределах поля')
            continue
        if not field[y][x] in abc:
            print('Этот ход уже был')
            continue
        return (x, y)

print('Привет. Это игра "Охотник за сокровищами". На карте спрятаны сундуки с сокровищами. Вам нужно их отыскать с помощью радара. Вводите координаты точек на карте и узнавайте расстояние до ближайшего сундука. Удачи!')
field = getNewMap()
chests = hideChests()
for attempt in range(MAX_ATTEMPTS):
    printMap(field)
    print('Осталось сундуков:', len(chests))
    print('Осталось попыток:', MAX_ATTEMPTS - attempt)
    move = getUserMove(field)
    x, y = move
    dist = radar(chests, move)
    if dist == 0:
        print('Вы нашли сундук!')
        chests.remove(move)
        field[y][x] = '@'
    elif dist < 10:
        print('Расстояние до ближайшего сундука:', dist)
        field[y][x] = str(dist)
    else:
        print('Ничего не найдено')
        field[y][x] = 'x'