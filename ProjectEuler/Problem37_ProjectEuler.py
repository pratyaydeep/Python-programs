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
def right_left(n):
    while(n>0):
        if prime(n) == False:
            return False
            break
        n = n // 10
    else:
        return True
def left_right(n):
    n = str(n)
    for i in range(len(n)-1):
        if prime(int(n[i+1:len(n)+1])) == False:
            return False
    else:
        return True
def check(n):
    if right_left(n) and left_right(n):
        return True
    else:
        return False
count = 0
total = 0
list = []
i = 10
while (count<11):
    if check(i):
        list.append(i)
        count += 1
        total += i
    i += 1
print (list)
print (total)