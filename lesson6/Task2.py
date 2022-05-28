class Road:
    def __init__(self, _length, _width, _kg, _sm):
        self._length = _length
        self._width = _width
        self._kg = _kg
        self._sm = _sm

    def mass(self):
        return self._length * self._width * self._kg * self._sm


class Count(Road):
    def __init__(self, _length, _width, _kg, _sm):
        super().__init__(_length, _width, _kg, _sm)
        self._kg = _kg
        self._sm = _sm

r = Count(20, 5000, 25, 5)

print(r.mass())
