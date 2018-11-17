my_file = open('sudoku.txt', 'r')
my_list = []
for i in range(50):
    table = []
    for i in range(10):
        line = my_file.readline().strip('\n')
        table.append(line)
    table = table[1:]
    my_list.append(table)
my_file.close()


