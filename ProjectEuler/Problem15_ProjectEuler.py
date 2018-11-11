# Ham can bang 2 chuoi
def equalize(m,n):
    if len(m) < len (n):
        for i in range(len(m),len(n)):
            m += "0"
    elif len(n) < len(m):
        for i in range(len(n),len(m)):
            n += "0"
    return m,n
# Ham cong 2 chuoi
def addition(m,n):
    result = ""
    m = m[::-1]
    n = n[::-1]
    m,n = equalize(m,n)
    remember = 0
    for i in range(len(m)):
        sum = int(m[i]) + int(n[i]) + remember
        remember = sum // 10
        result += str(sum % 10)
    if remember != 0:
        result += str(remember)
    result = result[::-1]
    return result
# Quy hoach dong
def f(m,n):
    if m == 0:
        return "1"
    elif n == 0:
        return "1"
    else:
        return addition(f(m-1,n),f(m,n-1))
import sys
sys.setrecursionlimit(1500)
print (f(20,20))
