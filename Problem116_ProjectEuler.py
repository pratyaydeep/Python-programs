def count(m):
    f = [1 for i in range(m)]
    f.append(2)
    for i in range(m+1,51):
        new = f[i-1] + f[i-m]
        f.append(new)
    return f[50]

print (count(2) + count(3) + count(4) - 3)