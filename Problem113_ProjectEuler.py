# So so increase co n chu so la (8+n)Cn
# So so decrease co n chu so la (9+n)Cn-1 do co truong hop 000..0
# So so vua increase vua decrease co n chu so la 9 iii..i
# Cac so nho hon 10^100 thi co 1,2,..,100 chu so
# S = tong (8+n)Cn (voi n=1-100) = 109C9 - 1
# T = tong(9+n)Cn (voi n= 1-100) - 100 = 110C10 - 101
S = 1
for i in range(1,10):
    S *= (100+i)
for i in range(1,10):
    S //= i
S -= 1
T = 1
for i in range(1,11):
    T *= (100+i)
for i in range(1,11):
    T //= i
T -= 101
print (S + T - 9 * 100)
