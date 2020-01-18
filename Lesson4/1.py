# -*- coding: utf-8 -*-

import sys

prod, rate, prize = map(float, sys.argv[1:])
print('Your salary is: ', (prod * rate) + prize)
