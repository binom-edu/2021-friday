import random

NUM_DIGITS = 3 # количество цифр в загадываемом числе
MAX_GUESS = 10 # количество попыток

# загадываем случайное число без повторяющихся цифр
def generateSecret():
    digits = '0 1 2 3 4 5 6 7 8 9'.split()
    random.shuffle(digits)
    # ans = ''
    # for i in range(NUM_DIGITS):
    #     ans = ans + digits[i]
    # return ans
    return ''.join(digits[:NUM_DIGITS])

# проверяем работу функции
print(generateSecret())