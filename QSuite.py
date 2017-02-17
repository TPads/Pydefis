import sys

sys.setrecursionlimit(9999)

i = 2313
j = 2374
values = dict()
nb = 0

values[1] = values[2] = 1


def q(n):
    if n not in values:
        values[n] = q(n - q(n - 1)) + q(n - q(n - 2))
    return values[n]


for x in range(i, j + 1):
    nb = nb + q(x)

print(nb)
