string = 'Un trèfle.'
string = string[string.find(' ') + 1: len(string)] + ' ' + string[:string.find(' ')]
print(string)
