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
# Xay dung day Fibonacci
Fibonacci = ["0","1","1"]
i=1
while (len(addition(Fibonacci[i],Fibonacci[i+1])) < 1000):
    Fibonacci.append(addition(Fibonacci[i],Fibonacci[i+1]))
    i += 1
print (i+2)
