'''Ap dung thuat toan o de bai ta tim ra tap sau [20,31,38,39,40,42,45] va tap nay gan toi uu nen 
ta chi can xet tat ca cac tap gan no bang cach +- 1,2,3 vao cac phan tu cua no va kiem tra xem tap do co thoa man ko.
Cach kiem tra ta gia su A = {a1<a2<..<a7}
Kiem tra cac tap con co 2 so va tap con co 1 so: a1+a2>a7
Kiem tra cac tap con co 3 so va tap con co 2 so: a1+a2+a3>a6+a7
Kiem tra cac tap con co 3 so voi nhau ta se kiem tra bang cach loai di 1 trong 7 so a1-a7 va chia doi tap con lai
Do vay ta chi can xet cac truong hop a1+a2+a6,a1+a3+a6,a1+a4+a6,a1+a4+a5,a1+a5+a6 
Kiem tra cac tap con co 3 so voi 4 so: a1+a2+a3+a4>a5+a6+a7
Tom lai ta can kiem tra a7<min(a1+a2,a2+a3-a1,...,a5+a6-a4,a1+a2+a3-a6,a1+..+a4-a5-a6) va lap ra 1 ham kiem tra tung bo 6 so'''

# Ham kiem tra tap 2 tap con 3 phan tu cua 1 tap 6 phan tu
def check1(a):
    if sum(a) % 2 == 1:
        return True
    else:
        if a[0] + a[1] + a[5] == sum(a) / 2:
            return False
        elif a[0] + a[2] + a[5] == sum(a) / 2:
            return False
        elif a[0] + a[3] + a[5] == sum(a) / 2:
            return False
        elif a[0] + a[3] + a[4] == sum(a) / 2:
            return False
        elif a[0] + a[4] + a[5] == sum(a) / 2:
            return False
        else:
            return True
# Ham kiem tra cac cap tap con 2 phan tu voi nhau
def check2(a):
    result = True
    for i in range(4):
        for j in range(i+1,5):
            for k in range(j+1,6):
                for l in range(k+1,7):
                    if a[i] + a[l] == a[j] + a[k]:
                        result = False
    return result

# Ham kiem tra cac cap tap con con lai cua tap 7 so
def check3(a):
    my_list = [a[0]+a[1], a[0]+a[1]+a[2]-a[5], a[0]+a[1]+a[2]+a[3]-a[4]-a[5]]
    if a[6] >= min(my_list):
        return False
    else:
        return True

def check(a):
    result = check2(a) and check3(a)
    for i in range(7):
        b = a[0:i]+a[i+1:7]
        result = result and check1(b)
    return result

A = [20,31,38,39,40,42,45]
# Bay gio ta se thay doi 6 gia tri cua A va kiem tra
S = sum(A)-20
result = ['313839404245']
# Gia su B=[20,a,b,c,d,e,f]
for a in range(A[1]-3,A[1]+4):
    for b in range(max(a+1,A[2]-3),A[2]+4):
        for c in range(max(b+1,A[3]-3),A[3]+4):
            for d in range(max(c+1,A[4]-3),A[4]+4):
                for e in range(max(d+1,A[5]-3),A[5]+4):
                    for f in range(max(e+1,A[6]-3),A[6]+4):
                        if check([20,a,b,c,d,e,f]) == True:
                            result.append(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))

print (set(result))