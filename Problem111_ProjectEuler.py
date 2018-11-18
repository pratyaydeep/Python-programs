from itertools import permutations,combinations
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

def findM(n): # Tim M(10,i) voi i # 0
    if n != 0:
        N = []
        number = str(n) * 9
        for j in range(10):
            if j!= n:
                for i in range(10):
                    new_number = int(number[:i]+str(j)+number[i:])
                    if prime(new_number):
                        N.append(new_number)
        if N == []:
            number = str(n) * 8
            digit = [x for x in range(10) if x != n]
            for x in digit:
                for y in digit:
                    for i in range(9):
                        for j in range(i+1,10):
                            new_number = int(number[:i]+str(x)+number[i:j]+str(y)+number[j:])
                            if prime(new_number) and new_number > pow(10,9) and new_number not in N:
                                N.append(new_number)
        return N
    else:
        N = []
        for i in range(1,10):
            number = str(i) + '0' * 8
            for k in range(1,10):
                for j in range(1,10):
                    new_number = int(number[:j] + str(k) + number[j:])
                    if prime(new_number):
                        N.append(new_number)
        return N

total = 0
for i in range(10):
    total += sum(findM(i))
print (total)

