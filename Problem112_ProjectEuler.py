def increase_decrease(n):
    list1 = list(str(n))
    list2 = list1.copy()
    list2.sort()
    if list1 == list2:
        return 'increase'
    else:
        list2.reverse()
        if list1 == list2:
            return 'decrease'
        else:
            return 'bouncy'

count = 0
i = 1
while count / i != 0.99:
    i += 1
    if increase_decrease(i) == 'bouncy':
        count += 1

print (i)