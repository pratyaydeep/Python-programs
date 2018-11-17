from itertools import combinations
from itertools import permutations

# Cac bo 4 chu so (10C4 = 210)
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = []
for i in combinations(A, 4):
    new_list = []
    for j in range(4):
        new_list.append(i[j])
    list1.append(new_list)

# Cac bo 3 phep tinh (4 ** 3 = 64)
B = ['+', '-', '*', '/']
list2 = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            new_list = []
            new_list.append(B[i])
            new_list.append(B[j])
            new_list.append(B[k])
            list2.append(new_list)

# Ham permutation
def permutation(C):
    result = []
    for i in permutations(C):
        new_list = []
        for j in range(4):
            new_list.append(i[j])
        result.append(new_list)
    return result

def operate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b

# Chu y dau () chi de quy dinh do uu tien cua cac phep tinh
# Khi ta xet tat ca cac hoan vi cua 4 so va tat ca cac phep toan co the thi ta chi can thuc hien tu trai sang phai la du ko can de y den dau ngoac
# Noi ro hon voi bo (a,b,c,d) va bo phep tinh (1,2,3): ta thuc hien phep tinh 1 voi a,b sau do lay kq thuc hien phep tinh 2 voi c roi lai lay kq thuc hien phep tinh 3 voi d
# Dong thoi 1 truong hop khac la thuc hien phep tinh 1 voi a,b ; thuc hien phep tinh 3 voi c,d roi thuc hien phep tinh 2 voi 2 kq nay

def compute1(D, E): # D la list cac so, E la list cac phep tinh
    result = operate(D[0], D[1], E[0])
    result = operate(result, D[2], E[1])
    result = operate(result, D[3], E[2])
    return result

def compute2(D, E):
    result1 = operate(D[0], D[1], E[0])
    result2 = operate(D[2], D[3], E[2])
    result = operate(result1, result2, E[1])
    return result

def find_max(F):
    numbers = []
    list3 = permutation(F)
    for j in range(len(list3)):
        for k in range(len(list2)):
            numbers.append(compute1(list3[j], list2[k]))
            numbers.append(compute2(list3[j], list2[k]))
    i = 1
    while i in numbers:
        i += 1
    return i - 1

max = 28
result = []
for i in range(len(list1)):
    if find_max(list1[i]) > max:
        max = find_max(list1[i])
        result = list1[i]

print (result)