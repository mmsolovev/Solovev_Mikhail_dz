class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машана поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости на {self.speed - 60}!')
        else:
            print(f'Текущая скорость {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости на {self.speed - 40}!')
        else:
            print(f'Текущая скорость {self.speed}')


class PoliceCar(Car):
    pass


a = TownCar(100, 'белый', 'Ford')
print(a.speed, a.color, a.name, a.is_police)
a.go()
a.stop()
a.turn('налево')
a.show_speed()

b = SportCar(100, 'красный', 'Ferrari')
b.go()
b.stop()
b.turn('направо')
b.show_speed()

c = WorkCar(41, 'черный', 'Volkswagen')
c.go()
c.stop()
c.turn('налево')
c.show_speed()

d = PoliceCar(160, 'синий', 'Audi', is_police=True)
print(d.speed, d.color, d.name, d.is_police)
d.go()
d.stop()
d.turn('напрво')
d.show_speed()
