# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm

from math import sqrt

# function to calculate the continued fraction
def cf(n):
    mn = 0.0
    dn = 1.0
    a0 = int(sqrt(n))
    an = int(sqrt(n))
    period = 0
    if a0 != sqrt(n):
        while an != 2*a0:
            mn = dn*an - mn
            dn = (n - mn**2)/dn
            an = int((a0 + mn)/dn)
            period += 1
    return period

count = 0

for i in range(10000):
    if cf(i) % 2 != 0:
        count += 1

print (count)





