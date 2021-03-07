def num_translate_adv(word):
    if word.istitle():
        return NUM_TRANSLATE_DICT.get(word.lower()).title()
    return NUM_TRANSLATE_DICT.get(word)


NUM_TRANSLATE_DICT = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять",
}

print(num_translate_adv('One'))
print(num_translate_adv('two'))
