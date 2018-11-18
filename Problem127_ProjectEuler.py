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

def compute_rad(n):
    primes = prime_factor(n)
    product = 1
    for i in primes:
        product *= i
    return (product,n)

data = []
for i in range(1,120001):
    data.append(compute_rad(i))
data.sort()
from math import gcd
hit = []
for c in range(3,120000):
    z = compute_rad(c)[0]
    for (x,a) in data:
        if x * z >= c/2:
            break
        else:
            b = c - a
            if b > a and gcd(a,b) == 1:
                y = compute_rad(b)[0]
                if x*y*z < c:
                    hit.append(c)

print (sum(hit))



