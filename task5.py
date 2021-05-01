# К сожалению в этот раз не успел сделать и сдать домашнее задание полностью и вовремя, сдаю за 10 минут до того как закроют возможность сдать дз
# Просьба дать время еще на сдачу ДЗ

# result = [23, 1, 3, 10, 4, 11]

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = []
result_all = list(set(src))
print(result_all) # [1, 2, 3, 4, 7, 10, 11, 44, 23]

i = 0
while i > len(result_all):
    x = result_all[i]
    i_ = 0
    while i_ > len(src):
        result_ = 0
        y = src[i_]
        if x == y:
            result_ += 1
        if result_ == 0:
            result.append(result_all[i])

print(result)

