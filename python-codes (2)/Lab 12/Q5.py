class Time:
    def __init__(self, h=0, m=0, s=0):
        self.total = h*3600 + m*60 + s

    def __add__(self, other):
        return Time(0, 0, self.total + other.total)

    def __sub__(self, other):
        diff = abs(self.total - other.total)
        return Time(0, 0, diff)

    def __repr__(self):
        h, remainder = divmod(self.total, 3600)
        m, s = divmod(remainder, 60)
        return f"{h:02d}:{m:02d}:{s:02d}"

t1 = Time(1, 30, 0)
t2 = Time(0, 45, 30)
print("Add:", t1 + t2)
print("Diff:", t1 - t2)