def square_root(n, digit):
  a = 5 * n
  b = 5
  while b < n * pow(10,digit):
    if a >= b:
      a = a - b
      b += 10
    else:
      a *= 100
      b = (b - 5) * 10 + 5
  return b // 10

my_list = [x for x in range(1,100) if (round(x ** 0.5) ** 2) != x]
sum = 0
for i in range(len(my_list)):
  number = str(square_root(my_list[i],100))
  for j in range(100):
    sum += int(number[j])
print (sum)