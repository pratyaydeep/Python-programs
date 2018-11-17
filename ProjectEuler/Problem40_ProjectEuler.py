n = 11
count = 11
list = [0,1,2,3,4,5,6,7,8,9,1,0]
while (count<=10**6):
    i = str(n)
    count += len(i)
    for j in range(len(i)):
        list.append(i[j])
    n += 1
product = 1
d = []
for i in range(7):
    product *= int(list[10**i])
    d.append(int(list[10**i]))
print (d)
print(product)