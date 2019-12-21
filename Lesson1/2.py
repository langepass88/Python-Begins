time = int(input('ВВедите время в секундах: '))
hours = (time // 3600) % 24
minutes = (time // 60) % 60
seconds = time % 60

print(f'Время в формате чч:мм:сс: {str(hours).rjust(2, "0")}:{str(minutes).rjust(2,"0")}:{str(seconds).rjust(2, "0")}')
