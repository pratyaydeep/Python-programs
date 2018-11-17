''' lists = [20617,22471,35683,45421,69271,75841,84283,87109,94813,114109, 116503, 119221, 140083, 157021, 162619, 167569, 
176569, 182401, 199627, 201679, 212101, 224269, 243007, 261259, 277621, 284029, 285109, 384109, 400399, 400993, 409687, 
440413, 449467, 452203, 474883, 504601, 525121, 579067, 582109, 590623, 615409, 661579, 674521, 732031, 734101, 736297, 
746539, 778669, 779281, 780109, 783169, 818053, 821537, 842389, 848833, 852091, 866527, 880567, 940417]'''

# Check prime
def prime(n):
    if n <= 1:
        return False
    elif n < 9:
        for i in range(2,n):
            if n % i == 0:
                return False
                break
        else:
            return True
    else:
        for i in range(2,int(n ** 0.5)+1):
            if n % i == 0:
                return False
                break
        else:
            return True

# Check permutation
def permutation(m,n):
    m = str(m)
    n = str(n)
    m = [int(m[i]) for i in range(len(m))]
    n = [int(n[i]) for i in range(len(n))]
    m.sort()
    n.sort()
    if m ==n:
        return True
    else:
        return False

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
  if number != 1:
    prime_divisors.append(int(number))
  return prime_divisors

# Compute phi
def phi(n,lists):
  phi = n
  for j in range(len(lists)):
    phi = phi * (lists[j] - 1)/ (lists[j])
  return int(phi)

primes = []
for i in range(2000,5000):
    if prime(i):
        primes.append(i)
min = 2
n = 0
for i in range(len(primes)):
    for j in range(i, len(primes)):
        if permutation(primes[i]*primes[j],(primes[i]-1)*(primes[j]-1)) and primes[i]*primes[j] < pow(10,7):
            if (primes[i]*primes[j]) / ((primes[i]-1)*(primes[j]-1)) < min:
                min = (primes[i]*primes[j]) / ((primes[i]-1)*(primes[j]-1))
                n = primes[i]*primes[j]
print (n)
