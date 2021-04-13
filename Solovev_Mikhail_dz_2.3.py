my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(my_list):
    if my_list[i].isdigit() or my_list[i][1:].isdigit():
        if my_list[i][0] == '+':
            my_list.insert(i, f'+0{my_list[i][1:]}')
            my_list.pop(i + 1)
            if my_list[i + 1] != '"':
                my_list.insert(i + 1, '"')
                my_list.insert(i, '"')
                i += 2
            else:
                i += 1
        elif len(my_list[i]) < 2:
            my_list.insert(i, f'0{my_list[i]}')
            my_list.pop(i + 1)
            if my_list[i + 1] != '"':
                my_list.insert(i + 1, '"')
                my_list.insert(i, '"')
                i += 1
            else:
                i += 1
        else:
            if my_list[i + 1] != '"':
                my_list.insert(i + 1, '"')
                my_list.insert(i, '"')
                i += 1
            else:
                i += 1
    else:
        i += 1
print(' '.join(my_list))
