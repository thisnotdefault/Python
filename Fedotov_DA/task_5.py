from random import choice


def get_jokes(amount=3, repeat_words=True):
    """
    This function generate some jokes

    :param amount: the amount jokes which you want to get
    :param repeat_words: repeat words True/False
    :return: return jokes list
    """
    jokes_list = []
    if repeat_words:
        for joke in range(amount):
            joke = f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"
            jokes_list.append(joke)
        return jokes_list

    else:
        _temp_nouns = nouns.copy()
        _temp_adverbs = adverbs.copy()
        _temp_adjectives = adjectives.copy()
        for _ in range(amount):
            _check_length = list(map(lambda *args: len(args), _temp_nouns, _temp_adverbs, _temp_adjectives))
            if len(_check_length) == 0:
                break

            joke = f"{choice(_temp_nouns)} {choice(_temp_adverbs)} {choice(_temp_adjectives)}"
            noun, adverb, adjective = joke.split()
            _temp_nouns.remove(noun)
            _temp_adverbs.remove(adverb)
            _temp_adjectives.remove(adjective)
            jokes_list.append(f"{noun} {adverb} {adjective}")

        return jokes_list


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes())
print(get_jokes(6, repeat_words=False))
