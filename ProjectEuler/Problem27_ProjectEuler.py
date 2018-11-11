# Ham kiem tra so nguyen to
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
# Ham tinh so so nguyen to nhieu nhat
def maximum_prime(a,b):
    count = 0
    i = 0
    while prime(i*i + a*i + b):
        i += 1
        count += 1
    return count

max = 0
product = 0
for i in range(-999,1000):
    if i % 2 != 0:
        for j in range(0,1001):
            if prime(j):
                if maximum_prime(i,j) > max:
                    max = maximum_prime(i,j)
                    product = i * j

print (product)
print (max)
