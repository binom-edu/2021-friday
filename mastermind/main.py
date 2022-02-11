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

# проверка ответа: подсчет быков и коров
def check(guess: str, secret: str) -> dict:
    ans = {'bulls': 0, 'cows': 0}
    for i in range(NUM_DIGITS):
        if guess[i] == secret[i]:
            ans['bulls'] += 1
        elif guess[i] in secret:
            ans['cows'] += 1
    return ans

# получение ответа пользователя и проверка корректности
def getUserMove() -> str:
    while True:
        guess = input('Введите ваше число: ')
        if len(guess) != NUM_DIGITS:
            print('Длина ответа не совпадает с загаданным числом')
            continue
        if not guess.isdigit():
            print('Ответ содержит недопустимые символы')
            continue
        return guess

# основная программа
print('Быки и коровы')
secret = generateSecret()
print(f'Загадано число из {NUM_DIGITS} цифр. У вас есть {MAX_GUESS} попыток, чтобы его отгадать.')
for i in range(MAX_GUESS):
    print('Попытка', i + 1)
    guess = getUserMove()
    result = check(guess, secret)
    print('Быки:', result['bulls'], 'Коровы:', result['cows'])
    if guess == secret:
        print('Вы выиграли!')
        break
else:
    print('Попытки закончились. Было загадано число', secret)