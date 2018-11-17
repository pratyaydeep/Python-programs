def is_pentagonal(n):
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False
def is_triangle(n):
    if (-1+(8*n+1)**0.5) % 2 == 0:
        return True
    return False
i = 143
while True:
    i += 1
    H_i=i*(2*i-1)
    if is_pentagonal(H_i) and is_triangle(H_i):
        break
print (H_i)