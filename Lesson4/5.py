from functools import reduce


def perv(prev_el, el):
    return prev_el * el


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(perv, my_list))
