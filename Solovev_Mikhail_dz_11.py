import random

class LotoCard:
    def __init__(self, player_type):
        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBER)


        self.player_type = player_type
        self._card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self._numbers = random.sample(range(1, self._MAX_NUMBER + 1), self._MAX_NUMBER_IN_CARD)

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    def has_number(self, number):
        for line in self._card:
            if number in line:
                return True
        return False

    def try_stoke_number(self, number):
        for index, line in enumerate(self._card):
            for num_index, number_in_card in enumerate(line):
                if number == number_in_card:
                    self._card[index][num_index] = '-'
                    self._numbers_stroked += 1
                    if self._numbers_stroked >= self._MAX_NUMBER_IN_CARD:
                        raise Exception(f'{self.player_type} победитель!')
                    return True
        return False

    def __str__(self):
        MAX_FIELD_LEN = 3
        header = f'\n{self.player_type}:\n'
        body = '\n'
        for line in self._card:
            for field in line:
                body += str(field).ljust(MAX_FIELD_LEN)
            body += '\n'
        return header + body


class LotoGame:
    def __init__(self, _human_player, _computer_player):
        self._human_player = _human_player
        self._computer_player = _computer_player
        self.barrel_sum = 0

    def start(self):
        _nums = [num for num in range(1, 91)]
        while True:
            barrel = random.choice(_nums)
            _nums.remove(barrel)
            self.barrel_sum += 1
            print(f'Новый бочонок: {barrel} (Осталось {90 - self.barrel_sum})')
            print(self._human_player)
            print(self._computer_player)
            a = input(f'Зачеркнуть цифру? (y/n)')
            if a == 'y':
                if LotoCard.has_number(self._human_player, barrel) == True:
                    LotoCard.try_stoke_number(self._human_player, barrel)
                else:
                    print('Вы проиграли')
                    break
            else:
                if LotoCard.has_number(self._human_player, barrel) == True:
                    LotoCard.try_stoke_number(self._human_player, barrel)
                else:
                    continue
            if LotoCard.has_number(self._computer_player, barrel) == True:
                LotoCard.try_stoke_number(self._computer_player, barrel)
            else:
                continue


human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')

LotoGame(human_player, computer_player).start()
