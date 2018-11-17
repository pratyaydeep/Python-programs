def prime(n):
    if n <= 1:
        return False
    elif n < 9:
        for i in range(2, n):
            if n % i == 0:
                return False
                break
        else:
            return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
                break
        else:
            return True


def prime_numbers(n):
    prime_numbers = []
    for i in range(2, n):
        if prime(i):
            prime_numbers.append(i)
    return prime_numbers


list1 = [x**2 for x in prime_numbers(7081) ]
list2 = [x**3 for x in prime_numbers(368) ]
list3 = [x**4 for x in prime_numbers(84) ]
numbers = []

for a in list1:
    for b in list2:
        for c in list3:
            total = a + b + c
            if total <= 5 * pow(10,7):
                numbers.append(total)

result = len(numbers)
numbers.sort()
for i in range(len(numbers)-1):
  if numbers[i] == numbers[i+1]:
    result -= 1
print (result)
