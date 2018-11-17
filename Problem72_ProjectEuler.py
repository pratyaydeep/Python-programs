#303908972655
#303963552391
# Find all prime prime_divisors
def prime_divisors(n):
  prime_divisors = []
  i = 2
  number = n
  while (number > 1 and i < pow(number,0.5)+1):
    if number % i == 0:
      number /= i
      if i not in prime_divisors:
        prime_divisors.append(i)
    else:
      i += 1
  if number != 1 and number not in prime_divisors:
    prime_divisors.append(int(number))
  return prime_divisors

# Compute phi
def phi(n):
  lists = prime_divisors(n)
  phi = n
  for j in range(len(lists)):
    phi = phi * (lists[j] - 1)/ (lists[j])
  return int(phi)

sum = 0
for i in range(2,pow(10,6)+1):
  sum += phi(i)
print (sum)