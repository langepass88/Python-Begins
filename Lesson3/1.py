def division(x, y):
    return x / y


while True:
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
    except ValueError:
        print('Вы ввели неверное число. Программа будет завершена')
        break
    if b == 0:
        print('Второе число не должно быть нулем. Попробуйте еще раз')
        continue
    print(division(a, b))
    break
