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
n = 35
while True:
    if prime(n):
        n += 2
    else:
        for i in range(1,int((n/2)**0.5)+1):
            if prime(n - 2 * i**2):
                break
        else:
            break
    n += 2
print (n)