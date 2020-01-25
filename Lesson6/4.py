class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')

    def police(self):
        if self.is_police:
            print('Полицейская машина')
        else:
            print('Не полицейская машина')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')
        else:
            print('Скорость нормальная')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')
        else:
            print('Скорость нормальная')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


bmw = Car(60, 'red', 'bmw')
bmw.go()
bmw.stop()
bmw.turn('прямо')
bmw.turn('назад')
bmw.turn('влево')
bmw.turn('вправо')
bmw.show_speed()

mercedes = TownCar(70, 'black', 'mercedes S500')
mercedes.go()
mercedes.stop()
mercedes.show_speed()
ferrari = SportCar(110, 'blue', 'ferrari')
ferrari.go()
ferrari.turn('влево')
lada = WorkCar(30, 'black', 'lada')
lada.go()
lada.show_speed()

uaz = PoliceCar(80, 'yellow', 'yaz')
uaz.go()
uaz.police()
