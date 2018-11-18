# Dung pt Pell
result = []
i = 1
x = [2] # (5b+-2)/2
y = [1] # 5L
i = 0
while len(result) < 12:
    if (x[i] % 5 == 2 or x[i] % 5 == 3) and x[i] > 3 and y[i] not in result:
        result.append(y[i])
    x.append(9*x[i]+20*y[i])
    y.append(4*x[i]+9*y[i])
    i += 1
    result.sort()

print (sum(result))