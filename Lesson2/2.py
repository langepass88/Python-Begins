my_list = []

while True:
    try:
        el = int(input('Введите целое число. Для прекращения ввода введите любое другое значение: '))
    except ValueError:
        print('Ввод завершен')
        break
    my_list.append(el)
print(f'Исходный массив: {my_list}')
for i in range(0, len(my_list), 2):
    try:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    except IndexError:
        break
print(f'Массив с измененными значениями: {my_list}')
