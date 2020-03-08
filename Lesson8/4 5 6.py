class DepotEq:
    depot = []

    """Метод показывает наличие товара на складе"""
    @staticmethod
    def show_depot():
        print('Наличие товара на складе: ')
        for el in DepotEq.depot:
            print(el)

    """Метод перемещения техники со склада в подразделение"""
    @staticmethod
    def move_dep(name, count, name_dep):
        if DepotEq.valid(name, count, name_dep):
            for el in DepotEq.depot:
                for key, val in el.items():
                    if name == val:
                        if count <= el['кол-во']:
                            el['кол-во'] -= count
                            if el['кол-во'] == 0:
                                DepotEq.depot.remove(el)
                            return print(f'Позиция: {name}, кол-во: {count} перемещена в подзразделение: {name_dep}')
                        else:
                            return print('Такого количества нет на складе')
            return print('Такого товара нет на складе')

    """Метод валидации"""
    @staticmethod
    def valid(name, count, name_dep):
        if not(isinstance(name, str)):
            print('Данные введены некорректно. Наименование должно быть строчным')
            return False
        elif not(isinstance(count, int)):
            print('Данные введены некорректно. Количество должно быть числом')
            return False
        elif not(isinstance(name_dep, str)):
            print('Данные введены некорректно. Название подразделения должно быть строчным')
            return False
        return True


class OfficeEq:
    _office_eq = []

    """Метод показывает наличие оргтехники"""
    @staticmethod
    def show_office_eq():
        for el in OfficeEq._office_eq:
            print(el)

    """Метод перемещает оргтехнику на склад"""
    @staticmethod
    def move_depot():
        DepotEq.depot.extend(OfficeEq._office_eq)
        print('Оргтехника перемещена на склад')

    def __init__(self, name, model, price, count):
        self.name = name
        self.model = model
        self.price = price
        self.count = count


class Printer(OfficeEq):
    def __init__(self, name, model, price, count, tech_print):
        super().__init__(name, model, price, count)
        self.tech_print = tech_print
        OfficeEq._office_eq.append({
            'наименование': self.name,
            'модель': self.model,
            'цена': self.price,
            'кол-во': self.count,
            'тип': self.tech_print
        })


class Scanner(OfficeEq):
    def __init__(self, name, model, price, count, sc_type):
        super().__init__(name, model, price, count)
        self.sc_type = sc_type
        OfficeEq._office_eq.append({
            'наименование': self.name,
            'модель': self.model,
            'цена': self.price,
            'кол-во': self.count,
            'тип': self.sc_type
        })


class Xerox(OfficeEq):
    def __init__(self, name, model, price, count, x_type):
        super().__init__(name, model, price, count)
        self.x_type = x_type
        OfficeEq._office_eq.append({
            'наименование': self.name,
            'модель': self.model,
            'цена': self.price,
            'кол-во': self.count,
            'тип': self.x_type
        })


x1 = Xerox('Xerox XX1', 'CC23456', 45000, 2, 'планшетный')
x2 = Xerox('Xerox XX2', 'CC23446', 45000, 1, 'портативный')
s1 = Scanner('HP Z1', 'XC6565', 13000, 3, 'цветной')
p1 = Printer('HP LJ125', 'MFP123', 45000, 4, 'лазерный')
OfficeEq.show_office_eq()
OfficeEq.move_depot()
DepotEq.show_depot()
DepotEq.move_dep('HP LJ125', 4, 'Отдел сбыта')
DepotEq.show_depot()
DepotEq.move_dep('Xerox XX1', 3, 'Бухгалтерия')
DepotEq.show_depot()
DepotEq.move_dep('HP LJ125i', 5, 'Отдел сбыта')
DepotEq.show_depot()
DepotEq.move_dep('HP LJ125i', '5', 'Отдел сбыта')
DepotEq.move_dep(123, 5, 'Отдел сбыта')
DepotEq.move_dep('HP LJ125i', 5, 123)
