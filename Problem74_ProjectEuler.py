from math import factorial
def length(n):
    chain = [n]
    count = 0
    while True:
        string = str(chain[count])
        count += 1
        number = 0
        for i in range(len(string)):
            number += factorial(int(string[i]))
        if number not in chain:
            chain.append(number)
        else:
            break
    return count

count = 0
for i in range(3,pow(10,6)):
    if length(i) == 60:
        count += 1
print (count)

