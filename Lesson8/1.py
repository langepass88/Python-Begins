class Data:
    data_str = input('Введите число в формате день-месяц-год:')

    def __init__(self):
        print(f'Вы ввели: {self.data_str}')

    @classmethod
    def num_transform(cls):
        numbers = cls.validation()
        try:
            print(f'День: {int(numbers[0])} Месяц: {int(numbers[1])} Год: {int(numbers[2])}')
        except TypeError:
            print('Программа выполнена некорректно')

    @staticmethod
    def validation():
        try:
            date_list = Data.data_str.split('-')
            if not (1 <= int(date_list[0]) <= 31):
                print('Некорректный формат ввода дня')
                return None
            elif not (1 <= int(date_list[1]) <= 12):
                print('Некорректный формат ввода месяца')
                return None
            elif not (1900 <= int(date_list[2]) <= 2020):
                print('Некорректный формат ввода года')
                return None
        except ValueError:
            return None
        else:
            return date_list


num = Data()
num.num_transform()
