# Ham kiem tra so nguyen to
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
# Theo dong du ta thay so so bi thay phai la boi cua 3, ta xet truong hop nho nhat la 3 va so nay nho nen chi co 1 chu so xuat hien dung 3 lan
def replace(n):
    digit = {
        "0": [],
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": [],
    }
    n = str(n)
    my_list = []
    for i in range(len(n)):
        digit[n[i]].append(i) # Dem so lan xuat hien cac chu so trong n
    for i in range(10):
        new_numbers = []
        if len(digit[str(i)]) == 3: # Chi thay the cac chu so co so lan xuat hien la 3
            for j in range(10):
                new_number = ""
                for k in range(len(n)):
                    if k not in digit[str(i)]:
                        new_number += n[k]
                    else:
                        new_number += str(j)
                new_number = int(new_number)
                if new_number >= pow(10,len(n)-1):
                    new_numbers.append(new_number)
        my_list.append(new_numbers)
    return my_list

def check(n):
    if not prime(n):
        return False
    else:
        my_list = replace(n)
        if len(my_list) == 0:
            return False
        else:
            for j in range(len(my_list)):
                count = 0
                for i in range(len(my_list[j])):
                    if prime(my_list[j][i]):
                        count += 1
                if count >= 8:
                    return True
            else:
                return False

n = 1
while not check(n):
    n += 1
print (n)
