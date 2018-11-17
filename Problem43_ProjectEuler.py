prime_numbers = [2,3,5,7,11,13,17]
from itertools import permutations
sum =[]
for i in range(10):
    sum.append(i)
numbers = list(permutations(sum))
def check(n):
    if n>10**9:
        n = str(n)
        for i in range(7):
            if int(n[i+1:i+4]) % prime_numbers[i] != 0:
                return False
        else:
            return True
    else:
        return False
total = 0
for i in range(len(numbers)):
    sum =''
    for j in range(10):
        sum += str(numbers[i][j])
    sum = int(sum)
    if check(sum):
        total += sum
print (total)
