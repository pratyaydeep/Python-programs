count = 0
for i in range(1,10):
    for j in range(1,22):
        if len(str(pow(i,j))) == j:
            count += 1
print (count)