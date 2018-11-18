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

def power(n,p):
    i = 0
    while n % pow(p,i) == 0:
        i += 1
    return i-1

i = 7
numbers = [2,3,5]
while i < pow(10,5):
    if prime(i):
        m = pow(2,power(i-1,2))*pow(5,power(i-1,5))
        if not A(m, i):
            numbers.append(i)
    i += 2
print (sum(numbers))
