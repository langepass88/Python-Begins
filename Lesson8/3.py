class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []

while True:
    el = input('Введите элемент списка. Для прекращения нажмите "q": ')
    if el == 'q':
        break
    try:
        if not(el.isdigit()):
            raise MyError('Вы ввели не число!')
    except MyError as err:
        print(err)
    else:
        el = int(el)
        my_list.append(el)


print(my_list)
