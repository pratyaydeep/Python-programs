# Tiep tuc khai thac pt Pell
# a>b,c la 3 canh tam giac ta co (a-b)|c
# Dat a-b = d; c = yd ta co a2+(a-d)2 = y2d2
# (2a/d - 1)2-2y2=-1 nghiem nho nhat 1,1 nghiem pt lien hop nho nhat (3,2) nen cthuc x=3x+4y, y=3y+2x
# a+b+c = (x+y)*d<10^8 nen y<50.000.000
Pell_solutions = []
x = [1] # (5b+-2)/2
y = [1] # 5L
i = 0
while 2*x[i]+3*y[i]<5*pow(10,7):
    x.append(3*x[i]+4*y[i])
    y.append(2*x[i]+3*y[i])
    i += 1
count = 0
print (x)
print (y)
for i in range(1,len(x)):
    S = x[i]+y[i]
    if S < pow(10,8):
        count += pow(10,8) // S

print (count)