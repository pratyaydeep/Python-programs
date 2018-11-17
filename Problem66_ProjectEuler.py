from math import sqrt

# function to calculate the continued fraction
def period(n):
    mn = 0.0
    dn = 1.0
    a = [int(sqrt(n))]
    i = 0
    period = 0
    if a[0] != sqrt(n):
        while a[i] != 2*a[0]:
            mn = dn*a[i] - mn
            dn = (n - mn**2)/dn
            a.append(int((a[0] + mn)/dn))
            period += 1
            i += 1
    while i<= 2*period:
        mn = dn * a[i] - mn
        dn = (n - mn ** 2) / dn
        a.append(int((a[0] + mn) / dn))
        i += 1
    return period, a

# Minimal solution of Pell equation is relative with the expression of sqrt(D)
def findp(n):
    b, a = period(n)
    p = []
    p.append(a[0])
    p.append(a[0]*a[1]+1)
    if b == 1 or b == 2:
        return p[1]
    else:
        for i in range(2,2*b):
            p.append(a[i]*p[i-1] + p[i-2])
    if b % 2 == 0:
        return p[b-1]
    else:
        return p[2*b-1]

max = 0
D = 0
for i in range(2,1001):
    if pow(round(pow(i,0.5)),2) != i:
        if findp(i) > max:
            max = findp(i)
            D = i
print (max)
print (D)