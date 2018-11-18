def square_number(n):
    if round(n ** 0.5) ** 2 == n:
        return True
    else:
        return False
result = []
# x+y,x-y,x+z,x-z,y+z,y-z lll a,b,c,d,e,f. Ta co the bieu dien b,e,f qua a,c,d cu the
# f=a-c, e=a-d, b=c-e=c+d-a, c va d cung tinh chan le, a<c+d
a = 100
solved = False
while not solved:
    c_start = int(pow(a**2/2,0.5)) + 1
    for c in range(c_start,a):
        d_start = int(pow(a**2 - c**2 + 1,0.5)) + 1
        if (c - d_start) % 2 != 0:
            d_start += 1
        for d in range(d_start,c,2):
            f = a**2 - c**2
            e = a**2 - d**2
            b = c**2 + d**2 - a**2
            if square_number(f) and square_number(e) and square_number(b):
                x = (c**2 + d**2)/2
                y = (2*a**2 - c**2 - d**2)/2
                z = (c**2 - d**2)/2
                solved = True
                result.extend([x,y,z])
                break
        if solved:
            break
    a += 1
print (sum(result))