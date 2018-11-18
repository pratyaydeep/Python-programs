# 1 tap co k phan tu la so nguyen to tu cac chu so 1-9. 2 < k<= 6
# Ta tim tat ca cac cach bieu dien 9:
'''
9 = 1+8, 2+7,3+6,4+5
=1+1+7,1+2+6,1+3+5,1+4+4,2+2+5,2+3+4,3+3+3
= 1+1+1+6, 1+1+2+5,1+1+3+4,1+2+2+4,1+2+3+3,2+2+2+3
= 1+1+1+1+5,1+1+1+2+4,1+1+1+3+3,1+1+2+2+3,1+2+2+2+2
= 1+1+1+1+2+3,1+1+1+2+2+2 
Do co toi da 4 so nguyen to co 1 chu so nen mot tong ko the co nhieu hon 4 so 1
Ta luot qua tat ca cac hoan vi cua 1-9 va xet xem co so nao thoa man ko
'''
def prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,int(n ** 0.5)+1):
            if n % i == 0:
                return False
                break
        else:
            return True

from itertools import permutations
string = '123456789'
permute = []
for x in list(permutations(string)):
    new = ''
    for y in x:
        new += y
    permute.append(new)

# Xac dinh cac cach khac nhau bieu dien 9
representation = [[0, 1, 9], [0, 2, 9], [0, 3, 9], [0, 4, 9], [0, 1, 2, 9], [0, 1, 3, 9], [0, 1, 4, 9], [0, 1, 5, 9],
                  [0, 2, 4, 9], [0, 2, 5, 9], [0, 3, 6, 9], [0, 1, 2, 3, 9], [0, 1, 2, 4, 9], [0, 1, 2, 5, 9],
                  [0, 1, 3, 5, 9], [0, 1, 3, 6, 9],[0, 2, 4, 7, 9], [0, 1, 2, 3, 4, 9], [0, 1, 2, 3, 5, 9],
                  [0, 1, 2, 3, 6, 9], [0, 1, 2, 4, 6, 9], [0, 1, 3, 5, 7, 9], [0, 1, 2, 3, 4, 6, 9],
                  [0, 1, 2, 3, 5, 7, 9]]

# [a,b,..] a, b la chi so bat dau, ket thuc cua so nguyen to
all = []

def check1(n):
    result = True
    for x in n:
        if not prime(x):
            result = False
    return result

def check2(n): # n la hoan vi cua '123456789'
    for x in representation: # Loop qua tat ca cac cach bieu dien va thu xem co thoa man ko
        length = len(x)
        numbers = []
        for i in range(length-1):
            new = int(n[x[i]:x[i+1]])
            numbers.append(new)
        if check1(numbers) and set(numbers) not in all:
            all.append(set(numbers))

for i in permute:
    check2(i)
print (all)
print (len(all))
