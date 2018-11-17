from itertools import permutations

def check(a,b):
  sum1 = []
  for i in range(len(a)):
        sum1.append(int(a[i]))
  sum1.sort()
  sum2 = []
  for i in range(len(b)):
        sum2.append(int(b[i]))
  sum2.sort()
  if sum1 == sum2:
    return True
  else:
    return False
def count(n):
    count = 0
    for i in range(n//2,2*n+1):
      if (n-i) % 3 == 0:
        if check (str(pow(n,3)),str(pow(i,3))):
          count += 1
    return count

n = 1020
while True:
    n += 1
    if count(n) == 5:
        break
print (n)