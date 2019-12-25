# Вариант со списком
month = int(input('Введите номер месяца: '))
year_list = ['', 'Зима', 'Зима',
             'Весна', 'Весна', 'Весна',
             'Лето', 'Лето', 'Лето',
             'Осень', 'Осень', 'Осень', 'Зима']

if 1 <= month <= 12:
    print(year_list[month])
else:
    print('Вы ввели неверно')

# Вариант со словарем
year_dict = {
    'Зима': [12, 1, 2],
    'Весна': [3, 4, 5],
    'Лето': [6, 7, 8],
    'Осень': [9, 10, 11]}


for season, months in year_dict.items():
    if month in months:
        print(season)
