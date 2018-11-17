a = [2]
for i in range(33):
    a.append(1)
    a.append(2*(i+1))
    a.append(1)
print (a)
numerator = [2,3]
for i in range(2,100):
    numerator.append(a[i]*numerator[i-1] + numerator[i-2])
string = str(numerator[9])
sum = 0
for i in range(len(string)):
    sum += int(string[i])
print (sum)