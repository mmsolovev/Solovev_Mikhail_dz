my_list = [57.8, 46.51, 97, 32.52, 41.14, 81.5, 64, 11.11, 35.8, 41.2, 8, 14.34, 99.99]
# A
new_list = []
for number in my_list:
    if '.' in str(number):
        num_list = str(number).split('.')
        r = num_list[0]
        kk = num_list[1]
        if len(kk) > 1:
            new_list.append(f'{r} руб {kk} коп')
        else:
            new_list.append(f'{r} руб {kk}0 коп')
    else:
        new_list.append(f'{number} руб 00 коп')
print(', '.join(new_list))
# B
print(id(my_list))
my_list.sort()
print(id(my_list))
sort_list = []
for number in my_list:
    if '.' in str(number):
        num_list = str(number).split('.')
        r = num_list[0]
        kk = num_list[1]
        if len(kk) > 1:
            sort_list.append(f'{r} руб {kk} коп')
        else:
            sort_list.append(f'{r} руб {kk}0 коп')
    else:
        sort_list.append(f'{number} руб 00 коп')
print(', '.join(sort_list))
# C
print(id(my_list))
new_list = my_list.copy()
new_list.reverse()
print(new_list)
print(id(new_list))
# D
print(', '.join(sort_list[-5:]))

