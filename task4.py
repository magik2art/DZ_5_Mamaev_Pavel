def num_of_max(source):
    result_ = []
    i = 1
    while i < len(source):
        if (source[i]) > (source[i - 1]):
            result_.append(source[i])
        i += 1
    yield result_


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for num in next(num_of_max(src)):
    result.append(num)

print('result = ', result)
