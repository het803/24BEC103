class MyString:
    def __init__(self, text=""):
        self.text = text

    def __iadd__(self, other):
        self.text += str(other)
        return self

    def toLower(self):
        self.text = self.text.lower()

    def toUpper(self):
        self.text = self.text.upper()

    def __repr__(self):
        return self.text

s = MyString("Hello")
s += " World"
print(s)
s.toLower()
print(s)
s.toUpper()
print(s)
