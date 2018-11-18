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

primes = []
i = 2
while len(primes) < 3 * pow(10,4):
    if prime(i):
        primes.append(i)
    i += 1
print (primes)

j = 1
while (2 * primes[j-1] * j) < pow(10,10) or j % 2 == 0:
    j += 1
print (j)