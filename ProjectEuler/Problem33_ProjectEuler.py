list = []
for i in range(10,100):
    if i % 10 != 0 and i % 11 != 0:
        a = i // 10
        b = i % 10
        for c in range(1,10):
            if c != b:
                j = 10*a+c
                if i/j == b/c and i/j < 1:
                    list.append(i)
                    list.append(j)
        for c in range(1,10):
            j = 10*c+a
            if i/j == b/c and i/j < 1:
                list.append(i)
                list.append(j)
        for c in range(1,10):
            j = 10*b+c
            if i/j == a/c and i/j <1:
                list.append(i)
                list.append(j)
        for c in range(1,10):
            if c != a:
                j = 10*c+b
                if i/j == a/c and i/j <1:
                    list.append(i)
                    list.append(j)
print (list)
product = 1
for i in range(4):
    product *= list[2*i+1]/list[2*i]
print (product)
