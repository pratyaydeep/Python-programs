my_file = open("keylog.txt","r")
my_list = []
numbers = []
for i in range(50):
   new_line = my_file.readline().strip('\n').split()
   string = new_line[0]
   my_list.append(string)
   for i in range(3):
       if int(string[i]) not in numbers:
           numbers.append(int(string[i]))
my_file.close()

def swap(i,j,new_list): #i,j la 2 so trong list number can doi cho
    a = new_list.index(i)
    b = new_list.index(j)
    if a > b:
        new_list[a] = j
        new_list[b] = i
    return new_list

for i in range(len(my_list)):
    a = int(my_list[i][0])
    b = int(my_list[i][1])
    c = int(my_list[i][2])
    numbers = swap(a,b,numbers)
    numbers = swap(b,c,numbers)

print (numbers)