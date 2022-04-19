import math

a = int(input("а" ))
b = int(input("b" ))
c = int(input("с" ))

if int((b*b-4*a*c) < 0):
    print('Корни уравнения отсутствуют')
else:
    d = math.sqrt(b*b-4*a*c)
    if d > 0:
        x1 = (-1 * b + d) / (a * 2)
        x2 = (-1 * b - d) / (a * 2)
        print(x1, x2, d)
    else:
        x1 = (-1 * b)/ (a * 2)
        print('один корень',x1)
