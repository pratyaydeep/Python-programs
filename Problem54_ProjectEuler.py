#Doc file
my_file = open("poker.txt","r")
player1 = []
player2 = []
for i in range(1000):
    turn = my_file.readline().rstrip("\n")
    p1 = ''
    p2 = ''
    for i in range(5):
        p1 += turn[3*i:3*i+2]
        p2 += turn[3*(i+5):3*(i+5)+2]
    player1.append(p1)
    player2.append(p2)
my_file.close()

# Chuyen gia tri bai theo thu tu
value = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13
}

# Chuyen 5 la bai thanh 5 so va 5 chat
def convert(card):
    number = ''
    type = ''
    for i in range(5):
        number += card[2*i]
        type += card[2*i+1]
    return number,type

# Ham dem so ki tu bang nhau
def count(string):
    count = 0
    for i in range(4):
        for j in range(i+1,5):
            if string[i] == string[j]:
                count += 1
    return count

# Ham kiem tra 5 so lien tiep ko?
def consecutive(string):
    new_number = []
    for i in range(5):
        new_number.append(value[string[i]])
    new_number.sort()
    for i in range(len(new_number)-1):
        if new_number[i+1] != new_number[i] + 1:
            return False
            break
    else:
        return True

# Phan loai bai
def score(card):
    number,type = convert(card)
    if count(type) == 10:
        if consecutive(number):
            if 'A' in number:
                return 10
            else:
                return 9
        else:
            return 6
    else:
        if count(number) == 6:
            return 8
        elif count(number) == 4:
            return 7
        elif count(number) == 3:
            return 4
        elif count(number) == 2:
            return 3
        elif count(number) == 1:
            return 2
        else:
            if consecutive(number):
                return 5
            else:
                return 1
# Sau khi chay thu ta thay ko co 4 loai 7,8,9,10
# Chi can so sanh 6 truong hop con lai
def sorting_number(card):
    number,type = convert(card)
    list = []
    for i in range(5):
        list.append(value[number[i]])
    list.sort()
    return list

def findresult(card1,card2):
    if score(card1) > score(card2):
        return 1
    elif score(card2) > score(card1):
        return 0
    else:
        list1 = sorting_number(card1)
        list2 = sorting_number(card2)
        if score(card1) == 6: #Flush
            for i in range(5):
                if list1[i] != list2[i]:
                    break
            if list1[i] > list2[i]:
                return 1
            else:
                return 0
        elif score(card1) == 5: #Straight
            if list1[0] > list2[0]:
                return 1
            else:
                return 0
        elif score(card1) == 4: #Three of a kind
            a = 0
            b = 0
            for i in range(5):
                if list1[i] == list1[i+1]:
                    a = list1[i]
                    break
            for i in range(5):
                if list2[i] ==  list2[i+1]:
                    b = list2[i]
                    break
            if a > b:
                return 1
            else:
                return 0
        elif score(card1) == 3: #Two pairs
            a1 = a2 = a3 = 0
            b1 = b2 = b3 = 0
            for i in range(4):
                if list1[i] == list1[i+1]:
                    a2 = list1[i]
                break
            for j in range(4):
                if list1[j] == list1[j+1] and list1[j] != a2:
                    a1 = list1[j]
                break
            for k in range(5):
                if list1[k] != a1 and list1[k] != a2:
                    a3= list1[k]
            for i in range(4):
                if list2[i] == list2[i+1]:
                    b2 = list2[i]
                break
            for j in range(4):
                if list2[j] == list2[j+1] and list2[j] != b2:
                    b1 = list2[j]
                break
            for k in range(5):
                if list2[k] != b1 and list2[k] != b2:
                    b3= list1[k]
            if a1 > b1:
                return 1
            elif a1 < b1:
                return 0
            else:
                if a2 > b2:
                    return 1
                elif a2 < b2:
                    return 0
                else:
                    if a3 > b3:
                        return 1
                    else:
                        return 0
        elif score(card1) == 2: # One pair
            a1 = 0
            b1 = 0
            for i in range(4):
                if list1[i] == list1[i+1]:
                    a1 = list1[i]
                    break
            del list1[i]
            del list1[i]
            for i in range(4):
                if list2[i] == list2[i+1]:
                    b1 = list2[i]
                    break
            del list2[i]
            del list2[i]
            if a1 > b1:
                return 1
            elif a1 < b1:
                return 0
            else:
                if list1[2] > list2[2]:
                    return 1
                elif list1[2] < list2[2]:
                    return 0
                else:
                    if list1[1] > list2[1]:
                        return 1
                    elif list1[1] < list2[1]:
                        return 0
                    else:
                        if list1[0] > list2[0]:
                            return 1
                        else:
                            return 0
        else: # High card, Cach khac la ghep thanh so roi so sanh
            if list1[4] > list2[4]:
                return 1
            elif list1[4] < list2[4]:
                return 0
            else:
                if list1[3] > list2[3]:
                    return 1
                elif list1[3] < list2[3]:
                    return 0
                else:
                    if list1[2] > list2[2]:
                        return 1
                    elif list1[2] < list2[2]:
                        return 0
                    else:
                        if list1[1] > list2[1]:
                            return 1
                        elif list1[1] < list2[1]:
                            return 0
                        else:
                            if list1[0] > list2[0]:
                                return 1
                            else:
                                return 0

total = 0
result = open("result.txt","w")
for i in range(1000):
    if score(player1[i]) == score(player2[i]) and findresult(player1[i],player2[i]) == 1:
        result.write(player1[i])
        result.write(str(score(player1[i])))
        result.write("\n")
        result.write(player2[i])
        result.write(str(score(player2[i])))
        result.write("\n")
    total += findresult(player1[i],player2[i])
print (total)
result.close()