numerator = [3]
denominator = [2]
for i in range(999):
    numerator.append(numerator[i] + 2*denominator[i])
    denominator.append(numerator[i] + denominator[i])
count = 0
for i in range(1000):
    if len(str(numerator[i])) == len(str(denominator[i])) + 1:
        count += 1
print (count)
