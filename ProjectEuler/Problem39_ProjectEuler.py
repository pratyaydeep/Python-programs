def number_of_triangle(n):
    count = 0
    a = n//4
    for a in range(n//4,n//2):
        for b in range(a):
            c = (a ** 2 + b ** 2) ** 0.5
            if a + b + c == n:
                count += 1
    return count
max = 0
result = 0
for i in range(25,1000):
    if number_of_triangle(i) > max:
        max = number_of_triangle(i)
        result = i

print (result)
