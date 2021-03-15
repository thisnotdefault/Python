tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Андрей', 'Станислав'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

if len(tutors) > len(klasses):
    difference = len(tutors) - len(klasses)
    for _ in range(difference):
        klasses.append("None")

couple = (x for x in zip(tutors, klasses))
