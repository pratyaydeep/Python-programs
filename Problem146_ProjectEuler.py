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

# n2+1, n2+3, n2+7, n2+9, n2+13, n2+27
# n = 0 mod 2
# n = 1,2 mod 3
# n = 0 mod 5
# n = 3,4 mod 7
# n = 10,80,130,200(mod 210)
# n = +-0,1,4,5 mod 11
# n = +-1,3,4 mod 13
# n = +-0,1,3,6,7 mod 17
# n = +-0,1,2,3,6,8 mod 19
mod = [10, 220, 290, 430, 550, 620, 640, 920, 1130, 1180, 1270, 1340, 1390, 1460,
       1550, 1600, 1810, 2090, 2110, 2180, 2300, 2440, 2510, 2720] #mod 2*3*5*7*13=2730
limit = 150*pow(10,6)
m = 2*3*5*7*13
def check(n):
    result = True
    m = n**2
    if not prime(m+1):
        result = False
    elif not prime(m+3):
        result = False
    elif not prime(m+7):
        result = False
    elif not prime(m+9):
        result = False
    elif prime(m+11):
        result = False
    elif not prime(m+13):
        result = False
    elif prime(m+17):
        result = False
    elif prime(m+19):
        result = False
    elif prime(m+21):
        result = False
    elif prime(m+23):
        result = False
    elif not prime(m+27):
        result = False
    return result

numbers = []
for k in range(limit//m+1):
    for j in mod:
        if check(m*k+j) and m*k+j<limit:
            numbers.append(m*k+j)

print (numbers)
print (sum(numbers))