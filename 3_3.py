string = input('Введите слово: ')
reversed = string[::-1]

if string == reversed:
    print(string, "\nПолиндром")
else:
    print(string, "\nНе полиндромом")
