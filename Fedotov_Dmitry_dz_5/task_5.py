src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
repeated_el = set()
unique_el = set()

for item in src:
    if item in repeated_el:
        unique_el.discard(item)

    elif item not in unique_el:
        unique_el.add(item)

    repeated_el.add(item)

result = [item for item in src if item in unique_el]
print(result)
