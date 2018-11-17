def is_triangle(n):
    if (-1+(8*n+1)**0.5) % 2 == 0:
        return True
    else:
     return False
def is_square(n):
    if (n**0.5) % 1 == 0:
        return True
    else:
        return False
def is_pentagonal(n):
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    else:
        return False
def is_hexagonal(n):
    if (1+(1+8*n)**0.5) % 4 == 0:
        return True
    else:
        return False
def is_heptagonal(n):
    if (3+(40*n+9)**0.5) % 10 == 0:
        return True
    else:
        return False
def is_octagonal(n):
    if (2+(4+12*n)**0.5) % 6 == 0:
        return True
    else:
        return False
def new_number(a,b):
    ''' Ham dua vao mot so b co 2 chu so va so a roi tra ve gia tri so co 4 chu so bat dau bang b va la so loai a'''
    number = []
    if a == 1:
        index = (-1+(8*b*100+1)**0.5) // 2 + 1
        number1 = index*(index+1) / 2
        number2 = (index+1)*(index+2) / 2
        if number1 // 100 == b:
            number.append(number1)
        if number2 // 100 == b:
            number.append(number2)
    elif a == 2:
        index = ((b*100)**0.5) // 1 + 1
        number1 = index ** 2
        number2 = (index+1) ** 2
        if number1 // 100 == b:
            number.append(number1)
        if number2 // 100 == b:
            number.append(number2)
    elif a == 3:
        index = (1+(24*b*100+1)**0.5) // 6 + 1
        number1 = index*(3*index-1)/2
        number2 = (index+1)*(3*index+2)/2
        if number1 // 100 == b:
            number.append(number1)
        if number2 // 100 == b:
            number.append(number2)
    elif a == 4:
        index = (1+(1+8*b*100)**0.5) // 4 + 1
        number1 = index*(2*index-1)
        number2 = (index+1)*(2*index+1)
        if number1 // 100 == b:
            number.append(number1)
        if number2 // 100 == b:
            number.append(number2)
    elif a == 5:
        index = (3+(40*b*100+9)**0.5) // 10 + 1
        number1 = index*(5*index-3)/2
        number2 = (index+1)*(5*index+2)/2
        if number1 // 100 == b:
            number.append(number1)
        if number2 // 100 == b:
            number.append(number2)
    return number

roster = [1,2,3,4,5]
from itertools import permutations
list0 = list(permutations(roster))

list1 = []
for a in range(1000, 10000):
    if is_octagonal(a):
        list1.append(a)
print (list1)

for i0 in range(len(list0)):
    for i1 in range(len(list1)):
        a = list1[i1] % 100
        if a >= 10:
            list2 = new_number(list0[i0][0],a)
            if len(list2) != 0:
                for i2 in range(len(list2)):
                    b = list2[i2] % 100
                    if b >= 10:
                        list3 = new_number(list0[i0][1],b)
                        if len(list3) != 0:
                            for i3 in range(len(list3)):
                                c = list3[i3] % 100
                                if c >= 10:
                                    list4 = new_number(list0[i0][2],c)
                                    if len(list4) != 0:
                                        for i4 in range(len(list4)):
                                            d = list4[i4] % 100
                                            if d >= 10:
                                                list5 = new_number(list0[i0][3],d)
                                                if len(list5) != 0:
                                                    for i5 in range(len(list5)):
                                                        e = list5[i5] % 100
                                                        if e >= 10:
                                                            list6 = new_number(list0[i0][4],e)
                                                            if len(list6) != 0:
                                                                for i6 in range(len(list6)):
                                                                    if list6[i6] % 100 == list1[i1] // 100:
                                                                        print (list1[i1]+list2[i2]+list3[i3]+list4[i4]+list5[i5]+list6[i6])



