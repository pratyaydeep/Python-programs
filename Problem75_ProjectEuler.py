n = 1500000
lists = {}
for i in range(n+1):
  lists[i] = []
for a in range(2,870):
  for b in range(1,a):
    d = 2*pow(a,2) + 2*a*b
    if d <= n:
      for c in range(1,n//d + 1):
        S = d * c
        triple = [2*a*b*c,(a**2-b**2)*c,(a**2+b**2)*c]
        triple.sort()
        if triple not in lists[S]:
          lists[S].append(triple)

count = 0
for i in range(len(lists)):
  if len(lists[i]) == 1:
    count += 1
print (count)