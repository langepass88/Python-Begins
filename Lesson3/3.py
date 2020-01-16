

def my_func(my_list):
    min_number = min(my_list)
    print(f'Самое минимальное число будет: {min_number}')
    my_list.remove(min_number)
    return sum(my_list)


num_1 = int(input('a = '))
num_2 = int(input('b = '))
num_3 = int(input('c = '))
print(f'Сумма наибольших двух аргументов равна: {my_func([num_1, num_2, num_3])}')
