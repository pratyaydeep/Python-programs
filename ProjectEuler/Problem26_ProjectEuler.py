# Xay dung phep chia
def divide(b):
    a = 1
    quotient = [0]
    remainder = [1]
    while True:
        while 10 * a < b:
            a = a * 10
            if 10 * a in remainder:
                for i in range(len(remainder)):
                    if remainder[i] == 10 * a:
                        starting_point = i
                        ending_point = len(remainder)
                        break
                break
            else:
                remainder.append(a)
                quotient.append(0)

        quotient.append(10 * a // b)
        a = (10 * a) % b
        if a not in remainder:
            remainder.append(a)
        else:
            for i in range(len(remainder)):
                if remainder[i] == a:
                    starting_point = i
                    ending_point = len(remainder)
            break
    return ending_point - starting_point
result = 0
find = 0
def max(a,b):
    if a > b:
        return a
    else:
        return b
for i in range(2,1000):
    if divide(i) > result:
        result = divide(i)
        find = i

print (result)
print (find)