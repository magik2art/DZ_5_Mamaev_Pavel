import argparse

parser = argparse.ArgumentParser(description='Введите целое число:')
parser.add_argument('indir', type=int)
args = parser.parse_args()
n = args.indir


def not_odd(max_num):
    list_not_odd_num = []
    n_ood = max_num
    if n_ood % 2 == 1:
        n_ood += 1
    for i in range(1, n_ood, 2):
        list_not_odd_num.append(i)
    yield list_not_odd_num


for n_ in next(not_odd(n)):
    print(">>> next(n)")
    print(n_)

print("...StopIteration...")

