minute = 60
hour = 3600
day = 86400

durations_list = []

number_of_values = int(input("Сколько значений вы хотите проверить ? "))

for value in range(number_of_values):
	amount = int(input("Укажите кол-во сек для проверки: "))
	durations_list.append(amount)

for duration in durations_list:

	if duration < minute:
		print(f"{duration} сек = {duration} сек")
	elif duration < hour:
		minutes = duration // minute
		seconds = duration % minute
		print(f"{duration} сек = {minutes} мин {seconds} сек")
	elif duration < day:
		hours = duration // hour
		minutes = duration % hour // minute
		seconds = duration % hour % minute
		print(f"{duration} сек = {hours} час {minutes} мин {seconds} сек")
	else:
		days = duration // day
		hours = duration % day // hour
		minutes = duration % day % hour // minute
		seconds = duration % day % hour % minute
		print(f"{duration} сек = {days} дн {hours} час {minutes} мин {seconds} сек")

