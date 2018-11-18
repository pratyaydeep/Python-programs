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
for i in range(1,100001):
    data.append(compute_rad(i))
data.sort()

print (data[9999][1])


