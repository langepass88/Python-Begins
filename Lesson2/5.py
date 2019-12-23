my_list = [7, 5, 3, 3, 2]
print(f'У нас есть набор натуральных чисел: {my_list}')

while True:
    try:
        num = int(input('Введите число: '))
    except ValueError:
        print('Программа завершена')
        break
    for i in range(len(my_list)):
        if num > my_list[i]:
            my_list.insert(i, num)
            break
        elif num <= my_list[-1]:
            my_list.append(num)
            break
    print(my_list)
