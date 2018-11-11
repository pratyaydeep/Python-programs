# Ham kiem tra so nguyen to
def prime(n):
    if n==2:
        return True
    elif (n<=9):
        for i in range(2,n):
            if n % i == 0:
                return False
                break
        else:
            return True
    else:
        for i in range(2,int(n ** 0.5)+1):
            if n % i == 0:
                return False
                break
        else:
            return True
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

total = ""
for i in range(2,2000000):
    if prime(i):
        print (i)
        total = addition(total,str(i))
print(total)





