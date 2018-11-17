from itertools import combinations
A = [0,1,2,3,4,5,7,8]
list1 = []
for i in combinations(A,6):
    my_list = []
    for j in range(6):
        my_list.append(i[j])
    list1.append(my_list)

list2 = []
for i in combinations(A,5):
    my_list = []
    for j in range(5):
        my_list.append(i[j])
    my_list.append(6)
    my_list.append(9)
    list2.append(my_list)

list3 = []
for i in combinations(A,4):
    my_list = []
    for j in range(4):
        my_list.append(i[j])
    my_list.append(6)
    my_list.append(9)
    list3.append(my_list)

main_list = list1 + 2 * list2 + list3 # So bo 6 chu so khac nhau

def check(a,b): # Ham kiem tra xem 2 arrangement co thoa man ko
    numbers = []
    for i in range(len(a)):
        for j in range(len(b)):
            numbers.append(10*a[i]+b[j])
            numbers.append(10*b[j]+a[i])
    for i in range(1,10):
        if i ** 2 not in numbers:
            return False
            break
    else:
        return True
print (check([0,5,6,7,8,9], [1,2,3,4,6,8,9]))
count = 0
for i in range(len(main_list)):
    for j in range(i,len(main_list)):
        if check(main_list[i],main_list[j]):
            count += 1

print (count)