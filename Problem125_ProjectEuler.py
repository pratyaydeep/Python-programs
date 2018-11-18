def palindromic(n):
    if int(str(n)[::-1]) == n:
        return True
    else:
        return False

#Sn = 1^2 + .. + n ^2
def S(n):
    return n * (n + 1) * (2*n + 1) // 6

consec_sum = []
for i in range(0,7072):
    for j in range(i+2,7074):
        number = S(j)-S(i)
        consec_sum.append(number)

total = 0

for i in set(consec_sum):
    if palindromic(i) and i < pow(10,8):
        total += i

print (total)
