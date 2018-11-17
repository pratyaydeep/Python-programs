def remove(i,n):
    while(n % i == 0):
        n = n/i
    return n
def count(n):
    if n == 1:
        return 0
    elif n == 2 or n ==3:
        return 1
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return 1 + count(remove(i,n))
        else:
            return 1
n = 646
while True:
    n += 1
    if (count(n)-4)**2 +(count(n+1)-4)**2 + (count(n+2)-4)**2 + (count(n+3)-4)**2 == 0:
        break
print (n)
