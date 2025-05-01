import math

class Solid:
    def __init__(self, kind, **kwargs):
        self.kind = kind.lower()
        self.args = kwargs

    def surface_area(self):
        if self.kind == 'cube':
            a = self.args['a']
            return 6 * a * a
        elif self.kind == 'sphere':
            r = self.args['r']
            return 4 * math.pi * r * r
        elif self.kind == 'cylinder':
            r, h = self.args['r'], self.args['h']
            return 2*math.pi*r*(r + h)
        else:
            raise ValueError("Unknown solid type")

    def volume(self):
        if self.kind == 'cube':
            a = self.args['a']
            return a ** 3
        elif self.kind == 'sphere':
            r = self.args['r']
            return 4/3 * math.pi * r ** 3
        elif self.kind == 'cylinder':
            r, h = self.args['r'], self.args['h']
            return math.pi * r * r * h
        else:
            raise ValueError("Unknown solid type")

cube = Solid('cube', a=1)
print("Cube SA:", cube.surface_area(), "Vol:", cube.volume())

sphere = Solid('sphere', r=2)
print("Sphere SA:", sphere.surface_area(), "Vol:", sphere.volume())

cylinder = Solid('cylinder', r=3, h=4)
print("Cylinder SA:", cylinder.surface_area(), "Vol:", cylinder.volume())