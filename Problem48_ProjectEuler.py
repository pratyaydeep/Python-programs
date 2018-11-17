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
    return str(int(result) % (10**10))
# Ham nhan chuoi voi mot so
def multiply(number,string):
    result = ""
    string = string[::-1]
    for i in range(len(string)):
        a = str(number * int(string[i]))
        if i > 0:
            for j in range(i):
                a += "0"
        result = addition(result,a)
    return result
# Ham so mu
def power(a,b):
    if b == 0:
        return "1"
    else:
        result = multiply(a,str(power(a,b-1)))
    return result

total = "0"
import sys
sys.setrecursionlimit(1500)
for i in range(1,1000):
    if i % 10 != 0:
        total = addition(total,power(i,i))
print(total)