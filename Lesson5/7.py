import json
from functools import reduce


def profit(rev, cost):
    rev = int(rev)
    cost = int(cost)
    if cost < rev:
        return rev - cost
    else:
        return 0


with open('firms.txt') as f_obj:
    lines = f_obj.readlines()
    my_dict = {el.split()[0]: profit(el.split()[2], el.split()[3])
               for el in lines if profit(el.split()[2], el.split()[3]) > 0}
    print(my_dict)
    sum_all = reduce(lambda x, y: x + y, my_dict.values())
    my_js = [my_dict, {'average_profit': sum_all}]
    print(my_js)

with open('my.json', 'w') as js_obj:
    json.dump(my_js, js_obj)
