class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def calculation(self, weight, depth):
        m = self._length * self._width * weight * depth
        print(f'{int(m/1000)} т')


a = Road(20, 5000)
a.calculation(25, 5)
