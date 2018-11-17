def check(n):
    a = (1+24*n) ** 0.5
    if a == int(a):
        b = (1+a)/6
        if b == int(b):
            return True
        else:
            return False
    else:
        return False
D = 0
i = 0
while D == 0:
    i += 1
    j = 1
    p_i = i*(3*i-1)/2
    # Kiem tra xem tong,hieu 2 so co la 1 so pentagonal ko?
    while (3*j+1<=p_i): # Khi j vuot qua gia tri tren thi p_i + p_j < p_j+1
        p_j = j*(3*j-1)/2
        if check(p_i+p_j):
            if check(2*p_i+p_j):
                D = p_i
                break
        j += 1
print (p_j)