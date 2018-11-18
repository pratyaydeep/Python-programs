'''
a = p**2 + p*q + q**2
b = p**2 + p*r + r**2
c = q**2 + q*r + r**2
Nghiem tong quat pt 1 la: m>n>0, m-n ko chia het cho 3 va
p = k(2mn+n2)
q = k(m2-n2)
a = k(m2+mn+n2)
'''
def square_number(n):
    if round(n ** 0.5) ** 2 == n:
        return True
    else:
        return False
# Liet ke tat ca cac cap (p,q) cua pt tren de thay m<347
result = []
limit = 120000
for m in range(2,347):
    for n in range(1,m):
        if (m-n) % 3 != 0:
            p = 2*m*n + n**2
            q = m**2 - n**2
            sum = p + q
            if sum < limit:
                for k in range(1,limit//sum+1):
                        result.append((k*q, k*p))

result = list(set(result))
my_dict = {}
for pair in result:
    my_dict[pair[0]] = []
    my_dict[pair[1]] = []
for pair in result:
    my_dict[pair[0]].append(pair[1])
    my_dict[pair[1]].append(pair[0])

Torr = []
for p in my_dict:
    for q in my_dict[p]:
            for r in my_dict[q]:
                if r != p and p in my_dict[r] and p+q+r<limit:
                    Torr.append(p+q+r)
final = list(set(Torr))
final.sort()
sum = 0
for x in final:
    sum += x
print (sum)
