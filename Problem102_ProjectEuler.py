my_file = open('triangles.txt','r')
my_list = []
for i in range(1000):
    line = list(map(int,my_file.readline().strip('\n').split(',')))
    my_list.append(line)
my_file.close()
print (my_list)
# Ta kiem tra O co thuoc tam giac ABC hay ko bang dien tich
# Cong thuc tinh dien tich tam giac ABC la: abs(1/2(xA-xC)(yB-yA) - (xA-xB)(yC-yA))
def area(xA,yA,xB,yB,xC,yC):
    return abs((xA-xC)*(yB-yA) - (xA-xB)*(yC-yA)) / 2

def check(xA,yA,xB,yB,xC,yC):
    if area(0,0,xA,yA,xB,yB) + area(0,0,xB,yB,xC,yC) + area(0,0,xA,yA,xC,yC) == area(xA,yA,xB,yB,xC,yC):
        return True
    else:
        return False

count = 0
for i in range(1000):
    if check(*my_list[i]):
        count += 1
print (count)