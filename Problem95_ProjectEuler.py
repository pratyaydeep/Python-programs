def count_power(i, n):
    count = 1
    while n % i == 0:
        count += 1
        n = n / i
    return count - 1


def sum_divisors(n):
    if n == 1:
        return 1
    elif n <= 3:
        return n + 1
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                k = count_power(i, n)
                return (pow(i, k + 1) - 1) // (i - 1) * sum_divisors(n / pow(i, k))
        else:
            return n + 1

def chain_length(n):
    numbers = [n]
    while True:
        m = numbers[len(numbers) - 1]
        if m != 1:
            new = sum_divisors(m) - m
        else:
            new = 1
        if new > pow(10, 6):
            return 0
        elif new not in numbers:
            numbers.append(new)
        else:
            if new == n:
                return len(numbers)
            else:
                return 0

max = 0
result = 0
for i in range(2, pow(10, 6) + 1):
    if chain_length(i) > max:
        max = chain_length(i)
        result = i

print (result)

# Co the tang toc do bang cach cho ham chain_length dung lai khi so them vao da duoc tinh chain_length roi
