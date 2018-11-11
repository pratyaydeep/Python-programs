def is_Palindrome(n):
    m = str(n)
    for i in range(0, len(m)):
        if m[i] != m[len(m) - 1 - i]:
            return False
            break
    else:
        return True


def max(a, b):
    if a >= b:
        return a
    else:
        return b


i = 999
result = 0
while (i > 99):
    j = i
    while (j > 99):
        if is_Palindrome(i * j):
            result = max(result, i*j)
            break
        else:
            j -= 1
    i -= 1
print (result)
