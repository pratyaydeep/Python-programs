# Ham dem so nghiem pt x1^2-x1x2+y1^2-y1y2 = 0 khi x2=i
# Cho i chay tu 2 - n ta se dem duoc so tam giac vuong ma ko co 2 canh goc vuong song song voi toa do
# Chu y kq can nhan voi 2 do tinh doi xung x2=i va x1=i co cung so nghiem.
def quad_solutions(n):
    count = 0
    for t in range(2,n+1):
        for i in range(n): #y2
            for j in range(i+1,n+1): #y1
                delta = t ** 2 - 4 * j * (j - i)
                if delta > 0:
                    sol1 = (t + delta ** 0.5)
                    sol2 = (t - delta ** 0.5)
                    if sol1 % 2 == 0:
                        count += 1
                        if sol2 > 0:
                            count += 1
                elif delta == 0:
                    count += 1
    return count

# So tam giac co 2 canh song song goc toa do la 3n^2

result = 3 * 50 ** 2 + quad_solutions(50)*2
print (result)