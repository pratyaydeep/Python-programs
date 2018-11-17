def check1(m,n):
    m = str(m)
    n = str(n)
    list1 = []
    list2 = []
    for i in range(len(m)):
        list1.append(m[i])
    for j in range(len(n)):
        list2.append(n[j])
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

def check2(m):
    for i in range(2,7):
        if not check1(i*m,m):
            return False
            break
    else:
        return True

i = 10**4
while not check2(i):
    i += 1
print (i)
