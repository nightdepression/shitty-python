def factor(iNumber):
    if iNumber <= 1:
        return 1
    else:
        return iNumber * factor(iNumber - 1)


iNumber = int(input('Число: '))
print('Факториал: ', factor(iNumber))
