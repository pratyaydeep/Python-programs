def is_Palindrome(n):
    m = str(n)
    for i in range(0, len(m)):
        if m[i] != m[len(m) - 1 - i]:
            return False
            break
    else:
        return True

def check(n):
    for i in range(49):
        n = int(n) + int(str(n)[::-1])
        if is_Palindrome(n):
            return True
            break
    else:
        return False

print (check(196))
count = 0
for i in range(1,10000):
    if check(i):
        count += 1
print (count)