from sys import argv
from utils import currency_rates


def get_currency_rates(*args):
    if len(args) == 1:
        return currency_rates(*args)


print(get_currency_rates(*argv[1:]))
