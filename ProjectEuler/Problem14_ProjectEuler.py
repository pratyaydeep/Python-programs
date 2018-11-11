def Collatzsequence(n):
    length = 1
    while(n>1):
        if n % 2 == 0:
            n = n /2
        else:
            n = 3 * n + 1
        length += 1
    return length

max_length = 0
strating_number = 0

for i in range(1,10**6):
    if Collatzsequence(i) > max_length:
        max_length = Collatzsequence(i)
        starting_point = i

print (starting_point)
print (max_length)
print (Collatzsequence(54))
