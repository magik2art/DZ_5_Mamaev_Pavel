

def name_class(max_num):
    list_of_students = []
    for i in range(max_num):
        if i < len(klasses):  # Сделал условие (Количество генерируемых кортежей не должно быть больше длины списка tutors.)
            list_of_students.append([tutors[i]] + [klasses[i]])
            # сделал условие по дз (Если в списке klasses меньше элементов, чем в списке tutors,
            # необходимо вывести последние кортежи в виде: (<tutor>, None)
        else:
            list_of_students.append(tutors[i] + [None])
    yield list_of_students


# переделал списки в кортежи согласно заданию
tutors = (
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
)
klasses = (
    '9А', '7В', '9Б', '9В',
    '8Б', '10А', '10Б', '9А'
)

num = len(tutors)
for key in next(name_class(num)):
    tutors_klasses = tuple(key)  # сделал вывод в кортеж согласно заданию
    print(tutors_klasses)

print(type(tutors_klasses))
