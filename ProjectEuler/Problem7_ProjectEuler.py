def prime(n):
    for i in range(2,n)):
        if n % i == 0:
            return False
            break
    else:
        return True
lists = []
i = 1
while (len(lists)<= 10001):
    i += 1
    if prime(i):
        lists.append(i)
print (lists[10000])