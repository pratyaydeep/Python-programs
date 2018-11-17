from math import factorial
def C(r,n):
    if r == 0:
        return 1
    else:
        return C(r-1,n) * (n-r+1) / r
count = 0
for n in range(23,101):
    count += n - 19
    for j in range(4,10):
        if C(j,n) > 10 ** 6:
            count += 2
print (count)