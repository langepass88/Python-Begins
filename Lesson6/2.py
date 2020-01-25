class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f'Данные приняты. Длина равна: {self._length}, ширина равна: {self._width}')

    def calculation(self, weight=25, thick=5):
        return print(f'Масса асфальта равна: {self._width * self._length * weight * thick}')


my_road = Road(200, 300)
my_road.calculation()
my_road.calculation(40, 3)
