a = int(input('a = '))
b = int(input('b = '))
i = 1
while a <= b:
    print(f'{i}-ый день: {a:.2f}')
    a = a + (a * 0.1)
    i = i + 1
print(f'{i}-ый день: {a:.2f}')
print(f'Ответ: на {i}-ый день спорстмен достиг результата - не менее {b} км.')
