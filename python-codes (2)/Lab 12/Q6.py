class Date:
    def __init__(self, day, month, year):
        self.d, self.m, self.y = day, month, year

    def __eq__(self, other):
        return (self.d, self.m, self.y) == (other.d, other.m, other.y)

    def __repr__(self):
        return f"{self.d:02d}-{self.m:02d}-{self.y}"

d1 = Date(1, 1, 2025)
d2 = Date(1, 1, 2025)
print("Same date?" , d1 == d2)
