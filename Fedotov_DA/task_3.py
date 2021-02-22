number = 0
word_end = "процент"

while True:
    number = input("Введите число от 0 до 20: ")
    if not number.isdigit():
        print("Нужно ввести число! Попробуйте еще раз.")
# в рамках данного практического задания
    elif int(number) > 20:
        print("Ваше число больше указанного диапазона")
    else:
        break

if int(number) == 1:
    print(f"{number} {word_end}")
elif int(number) == 2 or int(number) == 3 or int(number) == 4:
    print(f"{number} {word_end}а")
# задел на будущее если число > 20
# elif int(number) % 10 == 1:
#     print(f"{number} {word_end}")
# elif int(number) % 10 == 2 or int(number) % 10 == 3 or int(number) % 10 == 4:
#     print(f"{number} {word_end}а")
else:
    print(f"{number} {word_end}ов")
