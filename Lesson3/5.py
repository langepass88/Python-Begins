total = 0
ind = True
while ind:
    my_str = input('Введите строку, разделенную пробелом. \n'
                   'Для выхода нажмите клавишу "q". \n'
                   'Любые строчные символы кроме "q" будут игнорироваться: ')
    abc = my_str.split()
    print(abc)
    sum_abc = 0
    for el in abc:
        if el == 'q':
            ind = False
            break
        else:
            try:
                sum_abc += float(el)
            except ValueError:
                continue
    print(f'Сумма чисел в строке равна: {sum_abc}')
    total += sum_abc
    print(f'Общая сумма всех чисел: {total} \n'
          '==================================')
print('Программа завершена.')
