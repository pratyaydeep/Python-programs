#Ham xac dinh so mu
def power(p,n):
    i=1
    while (n % (p**i) == 0):
        i += 1
    return i-1
#Ham xac dinh so uoc
def number_of_divisors(n):
    if n == 1:
        return 1
    elif n == 2 or n == 3:
        return 2
    else:
        for i in range(2,int(n ** 0.5)):
            if n % i == 0:
                return (power(i,n) + 1) * number_of_divisors(n / (i ** power(i,n)))
                break
        else:
            return 2
#Ham tinh so nth-triangle dau tien
def triangle_number(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

i = 1
while (number_of_divisors(triangle_number(i)) <= 500):
    i += 1
print (i)
print (triangle_number(i))