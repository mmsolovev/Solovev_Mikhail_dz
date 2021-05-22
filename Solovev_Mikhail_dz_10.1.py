class Matrix:
    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.nums])

    def __add__(self, other):
        result = ''
        if len(self.nums) == len(other.nums):
            for line1, line2 in zip(self.nums, other.nums):
                if len(line1) == len(line2):
                    sum_line = [a + b for a, b in zip(line1, line2)]
                    result += ' '.join(map(str, sum_line)) + '\n'

                else:
                    return 'Wrong size'
        else:
            return 'Wrong size'
        return result


matrix1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
