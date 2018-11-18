# Ta se xap xi F(n) ~ ((1 + sqrt(5))/2) ^ n /sqrt(5)
# Lay log10 2 ve ta co log(F(n)= n * log((1+sqrt(5))/2) - log(sqrt(5)) = t
# De tinh 9 chu so dau tien cua F(n) ta chi viec lay 10^(phan le cua t + 8)
# Ham kiem tra 1-9 digital
from math import log10,sqrt
def digital(string):
    result = True
    for j in range(1,10):
        if str(j) not in string:
            result = False
    return result
F = [0,1]
i = 2
a = log10((1+sqrt(5))/2)
b = log10(sqrt(5))
while True:
    new = F[i-1] + F[i-2]
    F.append(new % pow(10,9))
    power = (a * i - b) % 1 + 8
    n = pow(10, power) // 1
    if digital(str(n)) and digital(str(F[i])):
      break
    i += 1
print (i)


