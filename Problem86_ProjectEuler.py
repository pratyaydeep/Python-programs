# Voi hinh hop axbxc (a<=b<=c) thi duong ngan nhat la (c ** 2 + (b + a) ** 2) ** 0.5
result = [2]
n = 3
while max(result) <= pow(10,6):
  limit = int(n * 5 ** 0.5)
  change = 0 # So hinh hop tang len khi n tang thi phai co it nhat mot canh la n
  for i in range(n+1,limit+1):
    j = round((i ** 2 - n ** 2) ** 0.5)
    if j ** 2 + n ** 2 == i ** 2:
      if j <= n:
        change += j // 2
      else:
        change += n - (j + 1) // 2 + 1
  result.append(result[len(result) - 1] + change)
  n += 1

print (n - 1)