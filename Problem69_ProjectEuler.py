'''We easily find that n/phi(n) = product of all numbers have the form of p/(p-1) with P is a prime divisor of n.
Therefore, the result max if and only if there are as a lot of p as possible and p is as small as possible. 
Thus n = 2 x 3 x 5 x..'''
def prime(n):
    if n <= 1:
        return False
    elif n < 9:
        for i in range(2,n):
            if n % i == 0:
                return False
                break
        else:
            return True
    else:
        for i in range(2,int(n ** 0.5)+1):
            if n % i == 0:
                return False
                break
        else:
            return True

prime_numbers = []
for i in range(100):
    if prime(i):
        prime_numbers.append(i)

n = 2
i = 0
while (n <= pow(10,6)):
    i += 1
    n *= prime_numbers[i]

print (n / prime_numbers[i])
