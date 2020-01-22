class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход: {self._income["wage"] + self._income["bonus"]}')


a = Position('Fedor', 'Ivanov', 'manager', 25000, 3000)
a.get_full_name()
a.get_total_income()
