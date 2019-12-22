while True:
    number = int(input('Введите целое положительное число: '))
    if number >= 0:
        break
i = 1
str_number = str(number)
max_number = int(str_number[0])

while i < len(str_number):
    if (int(str_number[i])) > max_number:
        max_number = int(str_number[i])
    i = i + 1
print(f'Самая большая цифра в числе {str_number} равняется: {max_number}')
