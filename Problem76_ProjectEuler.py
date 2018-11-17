table = [[0 for x in range(101)] for j in range(101)]
table [0][0] = 1
for j in range(1,100):
    table[1][j] = 1 # so cach bieu dien 0 bang tong cach so nguyen duong ko vuot qua j
for i in range(1,101):
    table[i][1] = 1 # khong co cach bieu dien so i boi cac so ko vuot qua 0
for i in range(2,101): # bieu dien so i
    for j in range(1,i+1): # cac so khong vuot qua j
        if j >= 2:
            if i-j >= j:
                table[i][j] = table[i][j-1] + table[i-j][j]
            else:
                table[i][j] = table[i][j-1] + table[i-j][i-j]

print (table[100][100] - 1)