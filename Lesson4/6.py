from itertools import cycle, count
n = int(input('ВВедите число: '))
for el in count(n):
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
