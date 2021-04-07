duration = int(input('Введите продолжительность промежутка времени: '))

if duration < 60:
    print(duration, 'сек')
elif duration < 3600:
    print(duration // 60, 'мин', duration % 60, 'сек')
elif duration < 86400:
    print(duration // 3600, 'ч', (duration % 3600) // 60, 'мин', (duration % 3600) % 60, 'сек')
else:
    print(duration // 86400, 'д', (duration % 86400) // 3600, 'ч', ((duration % 86400) % 3600) // 60, 'мин', ((duration % 86400) % 3600) % 60, 'сек')
