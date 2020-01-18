from itertools import cycle, count


for el in count(int(input('Введите стартовое число: '))):
    if el > 10:
        break
    else:
        print(el)
print('==================')

it = int(input('Сколько раз повторить элементы списка? '))
c = 0
for el in cycle('abc'):
    if c >= it:
        break
    print(el)
    c += 1
