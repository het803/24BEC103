class cplx:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return cplx(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return cplx(self.real - other.real, self.imag - other.imag)

    def __repr__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

a = cplx(59, 10)
b = cplx(57, -47)
print("a =", a)
print("b =", b)
print("a + b =", a + b)
print("a - b =", a - b)
