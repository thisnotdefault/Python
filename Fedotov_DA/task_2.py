pattern = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []

for el in pattern:
    if el.isdigit():
        number = int(el)
        new_list.extend(['"', f'{number:02d}', '"'])
    elif el.startswith('+') and el[1:].isdigit():
        number = int(el[1:])
        new_list.extend(['"', f'+{number:02d}', '"'])
    else:
        new_list.append(el)

print(new_list)

result_string = " ".join(new_list)
print(result_string)
