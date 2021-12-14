iNumber = input('Введите число: ''')
arr = [int(arr) for arr in str(iNumber)]

iTotal = 0
for iSec in arr:
    if iSec % 2 == 1:
        iTotal = iTotal + iSec * iSec
print('Сумма квадратов нечётных цифр в введённом числе равна:', iTotal)