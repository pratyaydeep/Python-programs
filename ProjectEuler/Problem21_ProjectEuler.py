# Compute the sum of proper divisors
def sum_divisors(n):
    result = 0
    if n == 1:
        return 1
    else:
        for i in range(1,n):
            if n % i == 0:
                result += i
        return result
# Ham kiem tra so amicable
def amicable(n):
    if sum_divisors(sum_divisors(n)) == n and sum_divisors(n) != n:
        return True
    else:
        return False
amicable_numbers = []

for i in range(2,10000):
    if amicable(i):
        if i not in amicable_numbers:
            amicable_numbers.append(i)
            amicable_numbers.append(sum_divisors(i))

total = 0
for i in range(len(amicable_numbers)):
    total += amicable_numbers[i]
print (amicable_numbers)
print (total)