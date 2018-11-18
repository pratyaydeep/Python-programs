# Y tuong nhu sau tuy nhien ko the tinh toan chinh xac trong python duoc
#http://www.mathblog.dk/project-euler-144-investigating-multiple-reflections-of-a-laser-beam/
def intersection(a, b, k): # Tim giao diem thu 2 cua duong thang di qua diem (a,b) va co he so goc la k
    a_new = (-2*k*b - 4*a + a*k**2)/(4 + k**2)
    b_new = (-b*k**2 - 8*k*a + 4*b)/(4 + k**2)
    return (a_new, b_new)
def new_slope(a, b, k): # Tim he so goc cua duong thang phan chieu cua duong thang di qua diem (a,b) va co he so goc la k
    l = -4*a/b # he so goc cua tiep tuyen cua elip tai (a,b)
    m = (k - l)/(1 + k*l) # he so goc giua duong thang di toi va tiep tuyen
    n = (l - m)/(1 + l*m) # he so goc cua duong thang phan chieu
    return n
x = [0.0, 1.4]
y = [10.1, -9.6]
k = -197/14
i = 1
while x[i]>0.1 or x[i]<-0.1 or y[i]<0:
    k = new_slope(x[i], y[i], k)
    (a, b) = intersection(x[i], y[i], k)
    x.append(a)
    y.append(b)
    i += 1

print (i)
