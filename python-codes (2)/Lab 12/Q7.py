class Weather:
    def __init__(self, params=None):
        self.params = params or []

    def __contains__(self, item):
        return item.lower() in (p.lower() for p in self.params)

    def __repr__(self):
        return f"Weather params: {self.params}"


# Demo
w = Weather(['Sunny', 'Humidity:60%', 'Temp:30C'])
print('Sunny' in w)
print('Rainy' in w)
print('Temp:30C' in w)
print('Humidity:60%' in w)
print(w)