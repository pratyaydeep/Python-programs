# Ta thay ta chi can xet cac cap tap con ko giao nhau ma co so phan tu bang nhau
# Voi n = 12 ta can xet cac cap tap con co do dai k = 2,3,4,5,6
# Voi cap tap con do dai k dau tien ta tim co 12C(2k) cach chon 2k so
# Tiep do ta tim xem tu tap 2k co bn cach chia doi de tong 2 tap con do co the bang nhau
# Chu y ta co 1 quan sat don gian neu chia doi [1,2,..,2k]thanh 2 tap con [xi],[yi]
# thi ta chi ko can so sanh tong cua chung khi yi > xi hoac yi < xi voi moi i, con lai deu co kha nang bang nhau
def check(a,b):
  result = False
  n = len(a)
  for i in range(n):
    if (a[i] - b[i])*(a[0]-b[0]) < 0:
      result = True
  return result

from itertools import combinations
def count(k):
    S = [i for i in range(2*k)]
    T = [list(x) for x in combinations(S,k)]
    count = 0
    for i in T:
        j = list(set(S) - set(i))
        i.sort()
        j.sort()
        if check(i,j):
            count += 1
    return count // 2

total = count(2) * 495 + count(3) * 924 + count(4) * 495 + count(5) * 66 + count(6)
print (total)