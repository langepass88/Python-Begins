name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = int(input('Введите возраст: '))
money = float(input('Введите кол-во денег в кармане: '))

print(f'Вас зовут: {name} {surname}. Ваше возраст: {age}. У вас в кармане: {money:.2f} рублей.')
