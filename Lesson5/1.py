out_f = open('text.txt', 'w')
while True:
    str_w = input('Введите строку. Чтобы закончить нажмите Enter :')
    if str_w == '':
        break
    out_f.write(f'{str_w}\n')
out_f.close()
