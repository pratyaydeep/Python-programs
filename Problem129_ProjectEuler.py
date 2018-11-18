# Nhan xet A(n) < n
from math import gcd
def A(n):
    if gcd(n,10) != 1:
        return 0
    else:
        x, k = 1, 1
        while x != 0:
            x = (x * 10 + 1) % n
            k += 1
        return k

n = pow(10,6)+1
while A(n) < pow(10,6):
    n += 2

print (n)


