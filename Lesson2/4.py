user_str = input('Введите строки через пробел: ')
str_list = user_str.split()

for i, word in enumerate(str_list):
    print(f'{i + 1}) {word[:10]}')
