# Dung ham sinh ta tinh duoc AG(x) = (3x2+x)/(1-x-x^2)
# Dua ve pt Pell co nghiem tong quat x=1.5x+2.5y; y=1.5y+0.5x tuy nhien no co 2 nghiem nho nhat la (7,1) va (7,-1)
result = []
x = [7]
y = [1]
a = [7]
b = [-1]
i = 0
while len(result) < 30:
    if x[i] % 5 == 2 and x[i] > 7 and ((x[i]-7)//5) not in result:
        result.append((x[i]-7)//5)
    x.append(1.5*x[i]+2.5*y[i])
    y.append(0.5*x[i]+1.5*y[i])
    if a[i] % 5 == 2 and a[i] > 7 and ((a[i]-7)//5) not in result:
        result.append((a[i]-7)//5)
    a.append(1.5*a[i]+2.5*b[i])
    b.append(0.5*a[i]+1.5*b[i])
    i += 1
    result.sort()
print (sum(result))