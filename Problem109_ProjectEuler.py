D = ['D' + str(i) for i in range(1,21)]
D.append('D25') # double bulleye
S = ['S' + str(i) for i in range(0,21)] # include miss
S.append('S25') # single bulleye
T = ['T' + str(i) for i in range(1,21)]
point = D + S + T

check_out = []
for x in D:
    for i in range(63):
        for j in range(i,63):
            check_out.append([x,point[i],point[j]])

def to_point(dart):
    if dart[0] == 'S':
        return int(dart[1:])
    elif dart[0] == 'D':
        return 2 * int(dart[1:])
    else:
        return 3 * int(dart[1:])
count = 0
for x in check_out:
    if to_point(x[0]) + to_point(x[1]) + to_point(x[2]) < 100:
        count += 1

print (count)
