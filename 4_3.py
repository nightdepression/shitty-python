iNumber = "Число: "
iResult = 0

while True:
    iNumberSec = input(iNumber)
    iNumber = "Введите следующее целое число: "
    if iNumberSec.lower() == 'стоп':
        break
    try:
        iResult += int(iNumberSec)
    except ValueError:
        print("Неверный тип символа")

print("Сумма введённых чисел равна: ", iResult)
