n = int(input('Введите число n: '))
str1 = ''
sum_n = 0
i = 0
while i < n:
    str1 = str1 + str(n)
    sum_n = sum_n + int(str1)
    i = i + 1
    print(f'n = {i}; число = {str1}; sum = {sum_n}')
print(f'Общая сумма равна: {sum_n}')
