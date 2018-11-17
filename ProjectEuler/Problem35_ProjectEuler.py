# Ham kiem tra so nguyen to
def prime(n):
    if n <= 1:
        return False
    elif n < 9:
        for i in range(2,n):
            if n % i == 0:
                return False
                break
        else:
            return True
    else:
        for i in range(2,int(n ** 0.5)+1):
            if n % i == 0:
                return False
                break
        else:
            return True
# Ham tao cac hoan vi vong tron cua 1 so
def rotate(n):
    n = str(n)
    rotations = []
    for i in range(len(n)):
        j = n[i:len(n)+1]+n[0:i]
        rotations.append(int(j))
    return rotations
#Ham kiem tra so nguyen to vong tron
def check(n):
    rotations = rotate(n)
    for i in range(len(rotations)):
        if prime(rotations[i]) == False:
            return False
    else:
        return True
list = [2]
for i in range(3,10**6):
    if prime(i) and '2' not in str(i):
        if check(i):
            list.append(i)
print (len(list))
