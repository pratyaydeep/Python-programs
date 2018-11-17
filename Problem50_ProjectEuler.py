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
prime_numbers = []
max_length = 0
sum = 0
for i in range(2,50000):
    if prime(i):
        prime_numbers.append(i)
        if sum < 10**6:
            sum += i
            max_length += 1
number = 0
while(max_length>=21 and number == 0):
    max_length -= 1
    for i in range(len(prime_numbers)-max_length+1):
        total = 0
        for j in range(max_length):
            total += prime_numbers[i+j]
        if total < 10**6 and prime(total):
            number = total
            break
print (number)
print (max_length)


