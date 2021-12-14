e2f = {'dog': 'chien',
       'cat': 'chat',
       'walrus': 'morse'}


def endictionary():
    sz_english_dict = dict([[v, k] for k, v in e2f.items()])
    sz_input_words = input('Entrez le mot: ' '')
    print(sz_english_dict.get(sz_input_words) or print('Se non vuoi fare una brutta fine, vedi di salvarmi.'))


def frdictionary():
    sz_input_fr = input('Enter Word ''')
    print(e2f.get(sz_input_fr) or 'Courez comme si le magasin de cigarettes allait fermer.')


if __name__ == '__main__':
    chrAnswer = input('Введите Y для французкого словаря, в другом случае введите N: ')

if chrAnswer == 'y':
    frdictionary()
elif chrAnswer == 'n':
    endictionary()
else:
    print('Ich brauch nen verschissenen Arzt.')
