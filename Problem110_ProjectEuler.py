# So nghiem cua pt 1/x + 1/y = 1/n bang so uoc cua n^2 // 2 + 1
def largest_power(n, p):
    count = 0
    while n % p ** count == 0:
        count += 1
    return count - 1
def count(n): # Dem so uoc cua n^2
    if n == 1:
        return 1
    else:
        for i in range(2, round(n ** 0.5) + 1):
            if n % i == 0:
                j = largest_power(n, i)
                return (2*j + 1) * count(n // (i ** j))
                break
        else:
            return 3

# Nhan xet so nho nhat phai co dang 2^x1*3^x2...
# Do 8,000,000 < 3^15 nen so do co ko qua 15 uoc nguyen to phan biet
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
max = 1
for i in primes:
    max *= i
# Goi x1,..,x15 la so mu cua cac so nguyen to
# De thay (xi) ko tang
# x1<7, x2<5, x3< 4, x4,..,x14 < 3, x15 < 2
my_list = []
# Sau day ta dung truy hoi de sinh ra tat ca cac bo so thoa man dieu kien tren va kiem tra
def generate(a):
  if len(a) == 15:
    my_list.append(a)
  else:
    b = len(a)
    if b == 0:
      c = 6
    elif b == 1:
      c = min(4,int(a[b-1]))
    elif b == 2:
      c = min(3,int(a[b-1]))
    else:
      c = min(2,int(a[b-1]))
    for i in range(c+1):
      c = a + str(i)
      generate(c)

generate('')

for i in my_list:
  number = 1
  for j in range(15):
    number *= pow(primes[j],int(i[j]))
  solutions = 1
  for j in range(15):
    solutions *= (2 * int(i[j]) + 1)
  if number < max and solutions > 8 * pow(10, 6):
    max = number

print (max)