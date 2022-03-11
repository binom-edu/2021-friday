def encrypt(message: str, key: int, decrypt=False) -> str:
    if decrypt:
        key *= -1
    res = ''
    for letter in message:
        pos = ALPHA.find(letter)
        if pos == -1:
            res += letter
        else:
            newpos = (pos + key) % len(ALPHA)
            res += ALPHA[newpos]
    return res

ALPHA = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

while True:
    var = input('Зашифровать - 0, расшифровать - 1: ')
    if var == '1':
        decrypt = True
    else:
        decrypt = False
    key = int(input('Укажите ключ: '))
    message = input('Введите сообщение для шифрования / дешифрования: ')
    print(encrypt(message=message, key=key, decrypt=decrypt))