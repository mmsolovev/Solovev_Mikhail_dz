percent = int(input('Введите количество процентов от 0 до 20: '))
ending = 0
if percent >= 0 and percent <= 20:
    if percent == 1:
        ending = ''
    elif percent == 2 or percent == 3 or percent == 4:
        ending = 'a'
    else:
        ending = 'ов'
    print('{} процент{}' .format(percent, ending))
else:
    print('Значение выходит за диапазон от 0 до 20')
