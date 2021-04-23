def odd_nums(max_num):
    num = 1
    while num <= max_num:
        yield num
        num += 2


odd_to_15 = odd_nums(7)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
