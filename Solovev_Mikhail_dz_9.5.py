class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} рисует')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} рисует')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} рисует')


a = Pen('Ручка')
a.draw()

b = Pencil('Карандаш')
b.draw()

c = Handle('Маркер')
c.draw()
