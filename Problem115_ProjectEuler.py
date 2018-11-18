f = [1 for i in range(50)]
f.append(2)
i = 50
while f[len(f)-1] < pow(10,6):
    i += 1
    new = f[i-1] + f[0]
    for j in range(i - 50):
        new += f[j]
    f.append(new)

print (i)