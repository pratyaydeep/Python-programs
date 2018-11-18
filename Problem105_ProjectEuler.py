my_file = open('p105_sets.txt','r')
lists = []
for i in range(100):
    line = list(map(int, my_file.readline().strip('\n').split(',')))
    line.sort()
    lists.append(line)
my_file.close()
# Phan tich mot chut do co dieu kien 1 va 2 nen dk 1 ta chi can cm:
# m = n // 2(n la do dai day) thi cac tap con m phan tu cua tap ban dau phan biet
# Dieu kien 2 chi can kiem tra cac tap con be nhat co k+1 phan tu phai lon hon tap con lon nhat co k phan tu
# Ham kiem tra dieu kien 2
def check2(a):
    n = len(a)
    m = n // 2
    result = True
    for i in range(2,m+2):
        if sum(a[0:i]) <= sum(a[(n-i+1):n]):
            result = False
    return result
# Ham kiem tra dieu kien 1
from itertools import combinations
def check1(a):
    n = len(a)
    m = n // 2
    S = [sum(x) for x in list(combinations(a,m))]
    T = set(S)
    if len(S) == len(T):
        return True
    else:
        return False

total = 0
for x in lists:
   if check1(x) and check2(x):
       total += sum(x)
print (total)