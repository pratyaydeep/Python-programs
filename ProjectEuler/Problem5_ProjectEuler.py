def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
            break
    else:
        return True
def power(p):
    i=1
    while (p ** i<=20):
        i += 1
    return i-1
lists = []
for i in range(2,21):
    if prime(i):
        lists.append(i)
result = 1
for i in lists:
    result *= i ** power(i)
print(result)
