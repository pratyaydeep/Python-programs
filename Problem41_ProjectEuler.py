def pandigital(number,n):
    number = str(number)
    if len(number) == n:
        for i in range(1,n+1):
            if str(i) not in number:
                return False
        else:
            return True
    else:
        return False
# Ham kiem tra so nguyen to
def prime(n):
    if n <= 1:
        return False
    elif n < 9:
        for i in range(2,n):
            if n % i == 0:
                return False
                break
        else:
            return True
    else:
        for i in range(2,int(n ** 0.5)+1):
            if n % i == 0:
                return False
                break
        else:
            return True
from itertools import permutations
def change(n):
    from itertools import permutations
    sum =[]
    for i in range(1,n+1):
        sum.append(i)
    return list(permutations(sum))
max = 0
for i in range(4,10):
    numbers = change(i)
    for j in range(len(numbers)):
        sum = ""
        for k in range(i):
            sum += str(numbers[j][k])
        sum = int(sum)
        if prime(sum) and sum > max:
            max =sum
print (max)