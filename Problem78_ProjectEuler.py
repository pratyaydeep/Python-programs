f = [1,1,2,3,5,7]
n = 6
def pent_num_1(n):
    return int(n * (3*n-1) / 2)
def pent_num_2(n):
    return int(n * (3*n+1) / 2)
while True:
    i = 1
    j = 1
    S = 0
    while pent_num_1(i) <= n:
        S += f[n-pent_num_1(i)] * pow(-1,i-1)
        i += 1
    while pent_num_2(j) <= n:
        S += f[n-pent_num_2(j)] * pow(-1,j-1)
        j += 1
    f.append(S)
    if S % (pow(10,6)) == 0:
        print (n)
        break
    else:
        n += 1
