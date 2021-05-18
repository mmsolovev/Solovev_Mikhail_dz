class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(f'{total_income}')


a = Position('Михаил', 'Соловьев', 'Директор', {'wage': 1000000, 'bonus': 100000})
print(a.name, a.surname, a.position, a._income)
a.get_full_name()
a.get_total_income()

b = Position('Василий', 'Пупкин', 'Садовник', {'wage': 100000, 'bonus': 10000})
b.get_full_name()
b.get_total_income()
