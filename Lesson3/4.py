def my_func(x, y):
    r = 1
    for i in range(abs(y)):
        r = r * x
    return 1 / r


while True:
    try:
        a = float(input('x = '))
        b = int(input('y = '))
    except ValueError:
        print('Вы ввели неверные числа. Программа будет завершена')
        break
    if b >= 0:
        print('Второе число должно быть отрицательным. Попробуйте еще раз: ')
        continue
    print(my_func(a, b))
    break
