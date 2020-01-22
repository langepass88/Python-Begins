import re
from functools import reduce


def my_f(my_str):
    my_list = re.findall('\d+', my_str)
    return reduce(lambda x, y: int(x) + int(y), my_list)


with open('subjects.txt') as f_obj:
    lines = f_obj.readlines()
    my_dict = {el.split(':')[0]: my_f(el.split(':')[1]) for el in lines}
    print(my_dict)
