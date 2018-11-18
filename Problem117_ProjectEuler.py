f = [1,1,2,4]
for i in range(4,51):
    new = f[i-1]+f[i-2]+f[i-3]+f[i-4]
    f.append(new)

print (f[50])
