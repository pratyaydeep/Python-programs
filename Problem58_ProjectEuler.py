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

# Kiem tra cac so tren duong cheo
n = 1
num_of_prime = 3
while ((num_of_prime / (4*n+1)) >= 0.1):
    for i in range(1,4):
        if prime((2*n+1) ** 2 + 2*(n+1)*i):
            num_of_prime += 1
    n += 1
print (2*n+1)