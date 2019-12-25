goods = []
good = {}
id_goods = 1
an_dict = {
    'название': [],
    'цена': [],
    'количество': [],
    'ед': []
}

num = int(input('Сколько единиц товара вы хотите внести: '))
while num >= id_goods:
    good_name = input('Введите имя: ')
    good_price = int(input('Введите цену: '))
    good_count = int(input('Введите кол-во: '))
    good_unity = input('Введите единицу измерения: ')
    good = (id_goods, {'название': good_name, 'цена': good_price, 'количество': good_count, 'ед': good_unity})
    goods.append(good)
    id_goods = id_goods + 1
    an_dict['название'].append(good_name)
    an_dict['цена'].append(good_price)
    an_dict['количество'].append(good_count)
    an_dict['ед'].append(good_unity)
    an_dict['ед'] = list(set(an_dict['ед']))
print('[')
for i in goods:
    print(i)
print(']')
print(an_dict)
