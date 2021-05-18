import time


class TrafficLight:
    __color = 'красный'

    def running(self):
        while True:
            print(f'{TrafficLight.__color}')
            time.sleep(7)
            __color = 'желтый'
            print(f'{__color}')
            time.sleep(2)
            __color = 'зеленый'
            print(f'{__color}')
            time.sleep(5)


a = TrafficLight()
a.running()
