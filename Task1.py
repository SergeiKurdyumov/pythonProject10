class Everfing:
    def __init__(self, my_attr):
        self.my_attr = my_attr
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

class Road:
    _surface_spec_gravity: float = 0.05
    width = Everfing("width")
    thickness = Everfing("thickness")
    length = Everfing("length")

    def __init__(self, length: [int, float], width: [int, float], thickness: [int, float]):
        self.length = float(length)
        self.width = float(width)
        self.thickness = float(thickness)

    def get_surface_gravity(self):
        try:
            return(self.length * self.width * self.thickness * self._surface_spec_gravity)

        except TypeError:
            return None

if __name__ == '__main__':
        road = Road(5000, 25, 20)
        road.length = 6000
        road.width = 30
        road.thickness = 25

        print ('масса равна', road.get_surface_gravity())