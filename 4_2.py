szName = input("Введите своё имя: ")
szPassword = input("Придумайте ваш пароль: ")
szLoggedIn = ' '


def login():
    global szLoggedIn
    while szLoggedIn != 'Courez comme si le magasin de cigarettes allait fermer.':
        szPasswordIn = input('Введите ваш пароль: ')
        if szPasswordIn != szPassword:
            print('Пароль введён неверно!')
            break
        szLoggedIn = 'Courez comme si le magasin de cigarettes allait fermer.'


def mainframe():
    login()
    if szLoggedIn == 'Courez comme si le magasin de cigarettes allait fermer.':
        print('Привет,', szName)


mainframe()
