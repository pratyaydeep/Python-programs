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

def max_prime(n):
    if n < 2:
        return 0
    else:
        prime_numbers = []  # cac so nguyen to ko vuot qua n
        for i in range(2, n + 1):
            if prime(i):
                prime_numbers.append(i)
        return prime_numbers[len(prime_numbers)-1]

table = [[0 for x in range(100)] for y in range(100)]
table[0][0] = 1
table[1][0] = 0
for x in range(2,100):
    if x % 2 == 0:
        table[x][2] = 1
    else:
        table[x][2] = 0

for x in range(3,100): # bieu dien so x
    prime_numbers = [] # cac so nguyen to ko vuot qua x
    for i in range(2, x+1):
        if prime(i):
            prime_numbers.append(i)
    for j in range(len(prime_numbers)):
        if j>= 1:
            if x >= 2 * prime_numbers[j]:
                table[x][prime_numbers[j]] = table[x][prime_numbers[j-1]] + table[x-prime_numbers[j]][prime_numbers[j]]
            else:
                table[x][prime_numbers[j]] = table[x][prime_numbers[j-1]] + table[x-prime_numbers[j]][max_prime(x-prime_numbers[j])]

a = 2
while True:
    if table[a][max_prime(a)] >= 5000:
        print (a)
        break
    else:
        a += 1

