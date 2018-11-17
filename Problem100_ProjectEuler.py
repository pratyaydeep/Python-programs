''' a, b are the number of blue discs and red discs respectively.
Ta dua dieu kien ve pt a^2 - (2b+1)a + b - b^2 = 0
Delta = 8b^2 + 1 la scp. Do do ta can giai pt pell u^2 - 8v^2 = 1
Khi do b = v con a = (2b+1+u)/2'''
u = [17]
v = [6]
i = 0
while 2*v[i] + (u[i]+1) / 2 <= pow(10,12):
    u.append(u[0]*u[i] + 8*v[0]*v[i])
    v.append(u[0]*v[i] + v[0]*u[i])
    i += 1
print (v[i] + (u[i]+1)/2 )
