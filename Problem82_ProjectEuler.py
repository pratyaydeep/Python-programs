my_file = open('p082_matrix.txt','r')
matrix = []
for i in range(80):
    new_line = list(my_file.readline().strip('\n').split(','))
    for j in range(len(new_line)):
        new_line[j] = int(new_line[j])
    matrix.append(new_line)
my_file.close()

'''Ta se quy hoach dong theo cot tu cot cuoi tro lai
O moi cot ta se tinh duong di nho nhat xuat phat tu moi o cua cot bang truy hoi theo cot truoc
Dau tien ta quet tu tren xuong roi xay dung truy hoi
Sau do quet tu duoi len va xay dung truy hoi'''

# Khoi tao gia tri dau khi o cot cuoi
min_path = []
for i in range(80):
    min_path.append(matrix[i][79]) # Do cot cuoi nen duong di ngan nhat chinh la o do

# Quy hoach dong theo cot
for i in range(0,79):
    j = 78 - i# Quet tu tren xuong cac o chi co the di sang phai hoac di len
    min_path[0] += matrix[0][j]
    for k in range(1,80):
        min_path[k] = min(min_path[k], min_path[k-1]) + matrix[k][j]# Quet tu duoi len chi co the di xuong hoac sang phai
    for k in range(0,79): # O cuoi cung chac chan min = min_path cu cong gia tri o do trong matrix nen ko can xet nua
        l = 78 - k
        min_path[l] = min(min_path[l], min_path[l+1] + matrix[l][j])

print (min(min_path))
