import math

n1 = abs(int(input()))
n2 = int(input())

if n2 <= 1:
    print(round(math.log(n1), 2))
else:
    print(round(math.log(n1, n2), 2))
