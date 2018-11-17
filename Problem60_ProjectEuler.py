def prime(n):
    if n <= 1:
        return False
    elif n < 9:
        for i in range(2,n):
            if n % i == 0:
                return False
                break
        else:
            return True
    else:
        for i in range(2,int(n ** 0.5)+1):
            if n % i == 0:
                return False
                break
        else:
            return True

def check(a,b):
  if prime(int(str(a)+str(b))) and prime(int(str(b)+str(a))):
    return True
  else:
    return False

list0 = []
for i in range(3,pow(10,4)):
    if prime(i):
        list0.append(i)

def new_list(number,list):
    new_list = []
    for i in range(len(list)):
        if check(number,list[i]):
            new_list.append(list[i])
    return new_list

min = 0
for a in range(len(list0)):
    list1 = new_list(list0[a],list0)
    if len(list1) != 0:
        for b in range(len(list1)):
            list2 = new_list(list1[b],list1)
            if len(list2) != 0:
                for c in range(len(list2)):
                    list3 = new_list(list2[c],list2)
                    if len(list3) != 0:
                        for d in range(len(list3)):
                            list4 = new_list(list3[d],list3)
                            if len(list4) != 0:
                                sum = list0[a] + list1[b] + list2[c] + list3[d] + list4[0]
                                if min == 0:
                                    min = sum
                                elif min > sum:
                                    min = sum
                                break
print(min)