def gcd(m,n):
    if m == 1 or n == 1:
        return 1
    else:
        if m >= n:
            p = m % n
            if p == 0:
                return n
            else:
                return gcd(n,p)
        else:
            p = n % m
            if p == 0:
                return m
            else:
                return gcd(m,p)
count = 1
for i in range(6,12001):
    for j in range(i//3+1, i//2+1):
        if gcd(j,i) == 1:
            count += 1

print (count)
