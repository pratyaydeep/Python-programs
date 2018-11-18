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
numbers = []
i = 5
while i < pow(10,6):
    if prime(i):
        numbers.append(i)
    i += 2
while not prime(i):
    i += 2
numbers.append(i)
# Extended Euclidean algorithm
def Euclid(a,b):
    r =  [a,b]
    s = [1,0]
    t = [0,1]
    i = 1
    while r[i] != 0:
        q = r[i-1] // r[i]
        r.append(r[i-1] -q*r[i])
        s.append(s[i-1]-q*s[i])
        t.append(t[i-1]-q*t[i])
        i += 1
    return [r[i-1],s[i-1],t[i-1]] # gcd(a,b) = r(i-1) = as(i-1) + bt(i-1)

total = 0
for i in range(len(numbers)-1):
    n = len(str(numbers[i]))
    [a,b,c] = Euclid(pow(10,n), numbers[i+1])
    b *= (numbers[i+1]-numbers[i])
    b %= numbers[i+1]
    total += int(str(b)+str(numbers[i]))
print (total)