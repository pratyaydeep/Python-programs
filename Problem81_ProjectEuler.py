my_file = open('matrix.txt','r')
matrix = []
for i in range(80):
    new_line = list(my_file.readline().strip('\n').split(','))
    for j in range(len(new_line)):
        new_line[j] = int(new_line[j])
    matrix.append(new_line)
my_file.close()

def min(a,b):
    if a < b:
        return a
    else:
        return b

table = [[0 for x in range(80)] for y in range(80)]
for i in range(80):
    for j in range(80):
        if i == j == 0:
            table[i][j] = matrix[i][j]
        elif i == 0:
            table[i][j] = table[i][j-1] + matrix[i][j]
        elif j == 0:
            table[i][j] = table[i-1][j] + matrix[i][j]
        else:
            table[i][j] = min(table[i-1][j],table[i][j-1]) + matrix[i][j]

print (table[79][79])
