# So nghiem cua pt 1/x + 1/y = 1/n bang so uoc cua n^2 // 2 + 1
def largest_power(n, p):
    count = 0
    while n % p ** count == 0:
        count += 1
    return count - 1
def count(n): # Dem so uoc cua n^2
    if n == 1:
        return 1
    else:
        for i in range(2, round(n ** 0.5) + 1):
            if n % i == 0:
                j = largest_power(n, i)
                return (2*j + 1) * count(n // (i ** j))
                break
        else:
            return 3

i = 100
while count(i) < 2001:
    i += 1
print (i)