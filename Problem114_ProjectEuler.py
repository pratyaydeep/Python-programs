# Bai nay ta se quy hoach dong theo do dai thanh
# Ta chia lam 2 truong hop o dau tien trang hoac do
# F(n) = F(n-1)+ F(n-4) + .. + F(0)
f = [1,1,1,2]
for i in range(4,51):
    new = f[i-1] + f[0]
    for j in range(i-3):
        new += f[j]
    f.append(new)
print (f[50])