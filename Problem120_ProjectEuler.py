def max_remainder(a):
    remainder = [2]
    for i in range(1,2*a,2):
        remainder.append((2*a*i) % pow(a,2))
    return max(remainder)

total = 0
for i in range(3,1001):
    total += max_remainder(i)
print (total)