# Nhan xet A(n) < n
from math import gcd
def A(n):
    x, k = 1, 1
    while x != 0:
        x = (x * 10 + 1) % n
        k += 1
    return k

composites = []

def prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,int(n ** 0.5)+1):
            if n % i == 0:
                return False
                break
        else:
            return True

i = 4
while len(composites) < 25:
    if gcd(i,10) == 1 and not prime(i):
        if (i-1) % A(i) == 0:
            composites.append(i)
    i += 1

print (sum(composites))
