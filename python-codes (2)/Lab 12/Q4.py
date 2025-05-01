import math

class RegularShape:
    def __init__(self, shape, **kwargs):
        self.shape = shape.lower()
        self.kw = kwargs

    def perimeter(self):
        if self.shape == 'square':
            s = self.kw['side']
            return 4 * s
        elif self.shape == 'circle':
            r = self.kw['r']
            return 2 * math.pi * r
        elif self.shape == 'triangle':
            a = self.kw['side']
            return 3 * a
        else:
            raise ValueError("Unknown shape")

    def area(self):
        if self.shape == 'square':
            s = self.kw['side']
            return s * s
        elif self.shape == 'circle':
            r = self.kw['r']
            return math.pi * r * r
        elif self.shape == 'triangle':
            a = self.kw['side']
            return (math.sqrt(3) / 4) * a * a
        else:
            raise ValueError("Unknown shape")

square = RegularShape('square', side=2)
print("Circumference:", square.perimeter(), "Area:", square.area())

circle = RegularShape('circle', r=1)
print("Circumference:", circle.perimeter(), "Area:", circle.area())

triangle = RegularShape('triangle', side=3)
print("Circumference:", triangle.perimeter(), "Area:", triangle.area())