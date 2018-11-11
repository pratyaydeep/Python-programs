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

# Ham luy thua
def factorial(number):
    if number == 1:
        return "1"
    else:
        return multiply(number,factorial(number-1))

result = factorial(100)
sum_digit = 0
for i in range(len(result)):
    sum_digit += int(result[i])

print(sum_digit)