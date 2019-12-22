time = int(input('Введите время в секундах: '))
hours = (time // 3600) % 24
minutes = (time // 60) % 60
seconds = time % 60

print(f'Время в формате чч:мм:сс: {hours:02}:{minutes:02}:{seconds:02}')
