numbers = input('Введите набор чисел через пробел: ')
new_file = open('numbers.txt', 'w')
new_file.write(numbers)
numbers = numbers.split()
sum_numbers = 0
for number in numbers:
    try:
        sum_numbers += int(number)
    except ValueError:
        continue
print(sum_numbers)
new_file.close()
