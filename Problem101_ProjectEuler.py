u = []
for i in range(1,12):
    new = 1 - i + i ** 2 - i ** 3 + i ** 4 - i ** 5 + i ** 6 - i ** 7 + i ** 8 - i ** 9 + i ** 10
    u.append(new)

'''Ki hieu Sk = x1^k + x2^k + ... + xn^k
Tk = x1x2..xk+ ... + xn-k+1xn-k+2..xn
Ta co cong thuc sau Sk = T1Sk-1 - T2Sk-2 + ... + (-1)^k*T(k-1)S1 + (-1)^(k+1)*kTk'''
# Ham tinh Sk theo k
def S(order, numbers):
    total = 0
    for x in numbers:
        total += pow(x, order)
    return total
# Ham tinh toan bo Tk
def T(numbers):
    T = [1]
    n = len(numbers)
    T.append(-S(1, numbers))
    for i in range(2, n+1):
        result = S(i, numbers)
        for j in range(1,i):
            result = result + pow(-1,j)*abs(T[j])*S(i-j, numbers)
        result = - result // i
        T.append(result)
    return T
# Ham tinh da thuc theo khai trien Lagrange bac n voi n+1 phan tu cua u
# Truoc het ta tinh he so:
def coefficient(i, n):
    numbers = list(range(1,n+1))
    numbers.remove(i+1)
    product = 1
    for x in numbers:
        product *= (i+1 - x)
    coefficient = T(numbers)
    new_coefficient = [(x * u[i])/ product for x in coefficient]
    return new_coefficient
# Tinh cac he so trong khai trien da thuc bac n
def lagrange(n):
    coef = [0 for i in range(n+1)]
    for i in range(0,n+1):
        i_coef = coefficient(i,n+1)
        for j in range(n+1):
            coef[j] += i_coef[j]
    return coef
# Dua vao da thuc trong noi suy Lagrange ta tinh phan tu FIT
def compute_FIT(n):
    coef = lagrange(n)
    result = 0
    for i in range(n+1):
        result += pow(n+2,n-i) * coef[i]
    return result

result = 1
for i in range(1,10):
    result += compute_FIT(i)
print (round(result))






