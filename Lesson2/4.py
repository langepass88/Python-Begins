user_str = input('Введите строки через пробел: ')
str_list = user_str.split()

for i in range(len(str_list)):
    print(f'{i + 1}) {str_list[i][:10] if len(str_list[i]) > 10 else str_list[i]}')
