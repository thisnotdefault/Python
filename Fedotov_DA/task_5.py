prices = [57.80, 46.51, 97, 56.14, 32.47, 12.51, 80.33, 12, 19.23, 2.5, 13.07, 5]
result = []

for price in prices:
    price = int(round(price * 100))
    rub = price // 100
    penny = price % 100
    result.append(f"{rub:2d} руб {penny:02d} коп ")

result_string = ", ".join(result)

print(f"Список цен в одну строку: {result_string}")
print(f"Id списка до сортировки по возрастанию {id(result)}")
result.sort()
print(f"Сортированный список: {result}")
print(f"Id списка после сортировки по возрастанию {id(result)}")
result_sorted = sorted(result)
result_sorted.sort(reverse=True)
print(f"Новый список после сортировки по убыванию(id:{id(result_sorted)}): {result_sorted}")
print(f"Цены пяти самых дорогих товаров: {result_sorted[:5]}")
