# Ham luy thua cho so nho
def power(a,b):
    if b == 0:
        return 1
    else:
        return a*power(a,b-1)
# Don gian bai toan bang viec kiem tra xem a co la luy thua cua mot so ko?
small_powers = []
my_list = {}
for i in range(2,11):
    if i not in small_powers:
        my_list[i] = []
        for j in range(1,7):
            if int(power(i,j)) <= 100:
                small_powers.append(power(i,j))
                my_list[i].append(j)
print (small_powers)
print (my_list)
total = 99 * (99-len(small_powers))
distinct_numbers = {}
for key in my_list:
    distinct_numbers[key] = []
    for i in range(len(my_list[key])):
        for j in range(2,101):
            if my_list[key][i] * j not in distinct_numbers[key]:
                distinct_numbers[key].append(my_list[key][i]*j)
    print(distinct_numbers[key])
    total += len(distinct_numbers[key])
print (total)