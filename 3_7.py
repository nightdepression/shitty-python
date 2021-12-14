import string
import random

iPassword = int(input('Желаемое число символов: '))
szPassword = ''.join(random.choices(string.ascii_letters + string.digits, k = iPassword))

print('Ваш пароль: ' + str(szPassword))
