class ComplexNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return 'Комплексное число: ' + str(self.re) + ' ' + str(self.im) + 'i'

    def __add__(self, other):
        return ComplexNum(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNum(self.re * other.re, self.im * other.im)


z1 = ComplexNum(1, -2)
print(z1)
z2 = ComplexNum(-3, 4)
print(z2)
z3 = z1 + z2
print(z3)
z4 = z1 * z2
print(z4)
