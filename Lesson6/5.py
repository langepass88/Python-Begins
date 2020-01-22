class Stationery:
    def __init__(self):
        self.title = 'ОАО "Кировские Канцелярские изделия"'

    def draw(self):
        print(f'Запуск отрисовки изделий фирмы: {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Выбрана ручка {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Выбран карандаш {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Выбран маркер {self.title}')


a = Stationery()
a.draw()
b = Pen()
b.draw()
c = Pencil()
c.draw()
d = Handle()
d.draw()
