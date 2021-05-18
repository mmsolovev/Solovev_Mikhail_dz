class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return str(self.nums + other.nums)

    def __sub__(self, other):
        if self.nums > other.nums:
            return str(self.nums - other.nums)
        else:
            return 'Ячеек в первой клетке меньше, чем во второй'

    def __mul__(self, other):
        return str(self.nums * other.nums)

    def __truediv__(self, other):
        return str(round(self.nums / other.nums))


a = Cell(24)
b = Cell(10)
print(a)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(10))
