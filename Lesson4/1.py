# -*- coding: utf-8 -*-

from sys import argv

script_name, prod, rate, prize = argv

prod = float(prod)
rate = float(rate)
prize = float(prize)
print('Your salary is: ', (prod * rate) + prize)
