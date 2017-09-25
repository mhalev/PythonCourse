import sys
from math import sqrt

if not (sys.argv[1]+sys.argv[2]+sys.argv[3]).isdigit():
    print('Один из коэффициентов не является числом!')
else:
    a, b, c, = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('Корни не могут быть найдены.')
    else:
        x1 = (-b + sqrt(d)) / 2 * a
        x2 = (-b - sqrt(d)) / 2 * a
        print(int(x1))
        print(int(x2))