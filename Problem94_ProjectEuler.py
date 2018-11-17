# Do dai 3 canh la a,a,a+1 hoac a,a,a-1
# Dien tich lan luot la S1 = (a+1)/4 *((3a+1)*(a-1)) ** 0.5 do do a phai le
# S2= (a-1)/4 * ((3a-1)*(a+1)) ** 0.5 do do a phai le
# Co the dung pt Pell de giai dieu kien so chinh phuong (3a+1, a-1) va (3a-1, a+1)
# Th1: (3a+1, a-1) la scp sau khi xet ucln 2 so ta dua ve pt Pell x^2 - 3y^2 = 1 trong do 4x^2 = 3a +1 <1 ti hay x < 16000
# Th2: (3a-1, a+1) la scp ta dua ve pt Pell x^2 - 3y^2 = -2 trong do 2x^2 = 3a -1 <1 ti nen x< 23000

sum = 0

# Tinh gia tri nghiem x cua pt Pell x^2 - 3y^2 = 1 voi nghiem nho nhat (2,1)
x = [1]
y = [0]
i = 0
while x[i] < 16000:
    x.append(2 * x[i] + 3 * y[i])
    y.append(2 * y[i] + x[i])
    i += 1
for j in range(1, len(x) - 1):# Nghiem dau tien cho tam giac 1,1,2 ko thoa man
    sum += pow(2*x[j], 2)

# Tinh gia tri x la nghiem cua pt Pell x^2 - 3y^2 = -2 voi nghiem nho nhat la (1,1)
a = [1]
b = [1]
i = 0
while a[i] < 23000:
    a.append(2 * a[i] + 3 * b[i])
    b.append(a[i] + 2 * b[i])
    i += 1
for j in range(1, len(a)-1):# Nghiem dau tien cho tam giac 1,1,0 ko thoa man
    sum += 2 * pow(a[j], 2)

print (sum)
