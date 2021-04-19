from random import choice


def get_jokes(num, repeat=True):
    """Returns num jokes formed from three random words taken from three lists (one from each)"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke = []
    for i in range(num):
        word1 = choice(nouns)
        word2 = choice(adverbs)
        word3 = choice(adjectives)
        joke.append(f'{word1} {word2} {word3}')
        if repeat is True:
            nouns.remove(word1)
            adverbs.remove(word2)
            adjectives.remove(word3)
        else:
            continue
    return joke


question1 = int(input('Введите сколько шуток вывести'))

print(get_jokes(question1))
