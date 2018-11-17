# Thuat toan A* http://www.policyalmanac.org/games/aStarTutorial.htm
# Xuat du lieu tu file sang matrix
my_file = open('p083_matrix.txt','r')
matrix = []
for i in range(80):
    new_line = list(my_file.readline().strip('\n').split(','))
    for j in range(len(new_line)):
        new_line[j] = int(new_line[j])
    matrix.append(new_line)
my_file.close()

# Tao bang tinh gia tri f,g,h cho tung o
f = [[0 for x in range(80)] for y in range(80)] # Tong quang duong
g = [[0 for x in range(80)] for y in range(80)] # Quang duong ngan nhat di tu o (0,0) den o (i,j)
h = [[0 for x in range(80)] for y in range(80)] # Quang duong uoc chung di tu o (i,j) den o (79,79)
open_list = [[0,0]]
close_list = []
min_val = 10000
max_val = 0

# Tim so lon nhat, nho nhat trong matrix
for i in range(80):
    min_val = min(min_val, min(matrix[i]))
    max_val = max(max_val, max(matrix[i]))

# Khoi tao gia tri ban dau cho f,g,h
for i in range(80):
    for j in range(80):
        g[i][j] = max_val * (i + j) + matrix[0][0]
        h[i][j] = min_val * (79*2 - i - j) # Cach uoc chung h nay dam bao k/c nay luon nho hon hoac bang k/c thuc te
        f[i][j] = h[i][j] + g[i][j]

# Tim phan tu trong open_list co f nho nhat
def find_min():
    a = open_list[0][0]
    b = open_list[0][1]
    result = f[a][b]
    for s in open_list:
        if result > f[s[0]][s[1]]:
            result = f[s[0]][s[1]]
            a = s[0]
            b = s[1]
    return a,b

while len(open_list) != 0 and [79,79] not in close_list:
    i,j = find_min()
    ad_i = [i - 1, i + 1,i,i]
    ad_j = [j,j,j - 1, j + 1]
    for k in range(4):
        s = ad_i[k]
        t = ad_j[k]
        if s in range(80) and t in range(80): # Kiem tra cac o ke co thuoc bang ko
            if [s,t] not in close_list: # Cac o ke khong trong close_list
                if [s,t] in open_list:# O ke da thuoc open_list
                    g[s][t] = min(g[s][t], g[i][j] + matrix[s][t])# Kiem tra xem g cu va g moi = g o[i,j] dang xet + gia tri o [s,t] cai nao be hon thi gan cho g[s][t]
                    f[s][t] = g[s][t] + h[s][t]
                else: # Cac o ke chua thuoc open_list
                    open_list.append([s,t]) # Them phan tu vao open_list
                    g[s][t] = g[i][j] + matrix[s][t]
                    f[s][t] = g[s][t] + h[s][t]
    close_list.append([i,j]) # Them (i,j) vao close_list
    open_list.remove([i,j]) # Xoa (i,j) o open_list

# Sau khi chay xong chi can in g[79][79]
print (g[79][79])






