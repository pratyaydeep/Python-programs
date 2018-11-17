# Check palindrome number
def is_Palindrome(n):
    m = str(n)
    for i in range(0, len(m)):
        if m[i] != m[len(m) - 1 - i]:
            return False
            break
    else:
        return True
# Convert a number to base 2
def base2(n):
    if n==1:
        return 1
    else:
        i = 0
        while (2**i<=n):
            i += 1
    i = i-1
    list = ""
    while i>=0:
        if n>=2**i:
            list += "1"
            n = n-2**i
        else:
            list += "0"
        i -= 1
    return (int(list))
total = 0
for i in range(1,10**6):
    if is_Palindrome(i) and is_Palindrome(base2(i)):
        total += i
print (total)

