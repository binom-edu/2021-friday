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
    for i in range(FIELD_HEIGHT):
        # for j in i:
        #     print(j, end='')
        # print()
        print(''.join(field[i]))

t = getNewMap()
printMap(t)