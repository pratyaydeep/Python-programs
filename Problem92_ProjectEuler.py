def check(n):
    if n == 89:
        return 1
    elif n == 1:
        return 0
    else:
        sum = 0
        number = str(n)
        for j in range(len(number)):
            sum += int(number[j]) ** 2
        return check(sum)

count = 0
for i in range(1, pow(10,7)+1):
    count += check(i)

print (count)

