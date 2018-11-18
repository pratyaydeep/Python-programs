my_file = open('p107_network.txt','r')
matrix = []
for i in range(40):
    line = my_file.readline().strip('\n').split(',')
    new_line = []
    for j in range(40):
        if line[j] == '-':
            new_line.append(0)
        else:
            new_line.append(int(line[j]))
    matrix.append(new_line)
my_file.close()

# Bai nay ta se su dung thuat toan Prim de tim cay bao trum co khung nho nhat
# https://en.wikipedia.org/wiki/Prim%27s_algorithm

initial_sum = 0
for x in matrix:
    initial_sum += sum(x)
initial_sum //= 2
# Bay gio ta se tim cay co khung nho nhat
final_sum = 0
trees = [0]
while len(trees) < 40:
    new_vertex = 0 # Them dinh moi
    smallest_edge = 1000 # Canh them nho nhat
    for i in trees:
        for j in range(40):
            if 0 < matrix[i][j] < smallest_edge:
                smallest_edge = matrix[i][j]
                new_vertex = j
    trees.append(new_vertex) # Cho diem moi vao cay
    final_sum += smallest_edge
    for i in trees:
        matrix[i][new_vertex] = 0
        matrix[new_vertex][i] = 0

print (initial_sum-final_sum)