szString = input('Хэш: ')
szResult = ""

for i in range(len(szString)):
    if szString[i].isdigit():
        szResult = szResult + (int(szString[i]) - 1) * szString[i + 1]
    else:
        szResult = szResult + szString[i]
print(szResult)
