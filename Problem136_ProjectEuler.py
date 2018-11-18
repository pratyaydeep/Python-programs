# De thay phuong trinh dua ve 3y^2-4yz = n
# Gia su y=u, 3y-4z =v trong do n =uv
# u+v phai chia het cho 4 va 3u>v.
# Do vay ta chi can lam nguoc lai cho chay het bo (u,v) va tang gia tri cua n = uv len 1
my_list = [0 for i in range(5*pow(10,7))]
limit = 5*pow(10,7)
for u in range(1,limit):
    if limit % u == 0:
        limit2 = min(3*u, limit//u)
    else:
        limit2 = min(3*u, limit//u+1)
    for v in range(1,limit2):
        if (u+v) % 4 == 0:
            my_list[u*v] += 1
count = 0
for i in my_list:
    if i == 1:
        count += 1
print (count)