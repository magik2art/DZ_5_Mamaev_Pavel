from collections import Counter


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

counter = [k for k, v in Counter(src).items() if v > 1] # выводим повторяющиеся цифры

i = 0
while i < len(counter):
    i_ = 0
    while i_ < len(src):
        if src[i_] == counter[i]:
            src.pop(i_)
        else:
            i_ += 1
    i += 1
print((src), "- Уникальные числа")
