def diagonal(n):
    if n == 1:
        return 25
    else:
        return diagonal(n-1) + 4*((2*n+1)**2) - 12*n
print (diagonal(500))