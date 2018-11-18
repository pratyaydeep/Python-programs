# Dung ham sinh ta tinh duoc Af(x) = x/(1-x-x^2)
# gia su x= a/b cho ta gia tri n nguyen duong
# Khi do n phai thoa man pt Pell: (5n+1)^2-5m^2=-4 nghiem nho nhat la 1,1
# phuong trinh pell x^2-5y^2=1 co nghiem nho nhat la (9,4) va nghiem huu ti nho nhat (3/2,1/2)
# Cong thuc truy hoi x = 1.5x+ 2.5y; y=1.5y+0.5x
# Ta co cong thuc x = 5n+1 nen ta chi can chon cac x dong du 1 mod 5
result = []
x = [1]
y = [1]
i = 0
while len(result) < 15:
    if x[i] % 5 == 1 and x[i] > 1 and ((x[i]-1)//5) not in result:
        result.append((x[i]-1)//5)
    x.append(1.5*x[i]+2.5*y[i])
    y.append(0.5*x[i]+1.5*y[i])
    i += 1
print (result[14])

