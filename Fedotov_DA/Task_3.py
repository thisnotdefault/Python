from collections import OrderedDict


def thesaurus(*args):
    result = {}
    for name in args:
        key = name[0].title()
        if key not in result:
            result[key] = []
        result[key].append(name)
    _result_dict = OrderedDict(sorted(result.items()))

    return dict(_result_dict)


print(thesaurus("Иван", "Мария", "Петр", "Андрей", "Федор", "Илья", "Павел", "Алексей", "Михаил", "Владислав"))
