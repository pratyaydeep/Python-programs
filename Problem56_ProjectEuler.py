max = 0
for a in range(2,100):
    for b in range(2,100):
        n = str(pow(a,b))
        sum = 0
        for i in range(len(n)):
            sum += int(n[i])
        if sum > max:
            max = sum

print (max)