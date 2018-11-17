# Xu li du lieu
my_file = open("triangle.txt","r")
my_list = []
for i in range(100):
   new_line = my_file.readline().strip('\n').split()
   for i in range(len(new_line)):
       new_line[i] = int(new_line[i])
   my_list.append(new_line)
my_file.close()

# Ham max
def max(a,b):
    if a>=b:
        return a
    else:
        return b
# Tinh bang gia tri max bang quy hoach dong
for i in range(1,100):
    for j in range(i+1):
        if j==0:
            my_list[i][j] = int(my_list[i-1][j]) + int(my_list[i][j])
        elif j==i:
            my_list[i][j] = int(my_list[i-1][j-1]) + int(my_list[i][j])
        else:
            my_list[i][j] = max(my_list[i-1][j],my_list[i-1][j-1]) + int(my_list[i][j])
# Tim max
result = 0
for j in range(100):
    result = max(result,my_list[99][j])
print(result)