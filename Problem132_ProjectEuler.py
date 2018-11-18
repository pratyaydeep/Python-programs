def prime_factor(n):
    if n <= 3:
        return [n]
    else:
        i = 2
        primes = []
        m = n
        while m > 1 and i <= int(n ** 0.5) + 1:
            if m % i == 0:
                primes.append(i)
                while m % i == 0:
                    m //= i
            i += 1
        if primes == []:
            primes.append(n)
        if m not in primes:
            primes.append(m)
    return primes
def A(m,n):
    x, k = 1, 1
    while k<m:
        x = (x * 10 + 1) % n
        k += 1
    if x == 0:
        return True
    else:
        return False
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
from math import gcd

i = 3
result = []
while len(result) < 40:
    if prime(i) and gcd(i,10)==1:
        j = gcd(pow(10,9),i-1)
        if A(j,i):
            result.append(i)
    i += 2
print (sum(result))

