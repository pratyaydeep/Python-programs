data = "75\
 95 64\
 17 47 82\
 18 35 87 10\
 20 04 82 47 65\
 19 01 23 75 03 34\
 88 02 77 73 07 63 67\
 99 65 04 28 06 16 70 92\
 41 41 26 56 83 40 80 70 33\
 41 48 72 33 47 32 37 16 94 29\
 53 71 44 65 25 43 91 52 97 51 14\
 70 11 33 28 77 73 17 78 39 68 17 57\
 91 71 52 38 17 14 91 43 58 50 27 29 48\
 63 66 04 68 89 53 67 30 73 16 69 87 40 31\
 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
# Ham max
def max(a,b):
    if a>=b:
        return a
    else:
        return b
# Xu li du lieu ve list
lists = []
for i in range(len(data)):
    if i % 3 == 0:
        lists.append(data[i]+data[i+1])
# Dua du lieu thanh mang 2 chieu bang cach dung list cua cac list
my_list = []
for i in range(15):
    a = (i * (i+1))//2
    b = ((i+1)* (i+2))//2
    new_list = []
    for j in range(a,b):
        new_list.append(lists[j])
    my_list.append(new_list)
# Tinh bang gia tri max bang quy hoach dong
for i in range(1,15):
    for j in range(i+1):
        if j==0:
            my_list[i][j] = int(my_list[i-1][j]) + int(my_list[i][j])
        elif j==i:
            my_list[i][j] = int(my_list[i-1][j-1]) + int(my_list[i][j])
        else:
            my_list[i][j] = max(my_list[i-1][j],my_list[i-1][j-1]) + int(my_list[i][j])
# Tim max
result = 0
for j in range(15):
    result = max(result,my_list[14][j])
print(result)
