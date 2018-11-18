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
# n = j ^ 3 va i = 3j^2+3j+1
i = 1
count = 0
while True:
    a =3*pow(i,2) + 3*i + 1
    if a > pow(10,6):
        break
    else:
        if prime(a):
            count += 1
    i += 1
print (count)