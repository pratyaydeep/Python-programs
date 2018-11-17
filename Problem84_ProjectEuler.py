'''squares = {
    0: 'GO',1: 'A1',2: 'CC1',3: 'A2',4: 'T1',5: 'R1',6: 'B1',7: 'CH1',8: 'B2',9: 'B3',
    10: 'JAIL',11: 'C1',12: 'U1',13: 'C2',14: 'C3',15: 'R2',16: 'D1',17: 'CC2', 18: 'D2', 19: 'D3',
    20: 'FP', 21: 'E1', 22: 'CH2', 23: 'E2', 24: 'E3', 25: 'R3', 26: 'F1', 27: 'F2', 28: 'U2', 29: 'F3',
    30: 'G2J', 31: 'G1', 32: 'G2', 33:'CC3', 34: 'G3', 35: 'R4', 36: 'CH3', 37:'H1', 38: 'T2', 39: 'H2'
}'''
'''CC = {1: 'Advance to GO', 2: 'Go to JAIL'}'''
'''CH = {1: 'Advance to GO', 2: 'Go to JAIL', 3: 'Go to C1', 4: 'Go to E3',
      5: 'Go to H2', 6: 'Go to R1', 7: 'Go to the next R',
      8: 'Go to next R', 9: 'Go to the next R', 10:'Go back 3 squares'}'''
CH_cards = {1: 0, 2: 10, 3: 11, 4: 24, 5: 39, 6: 5, 7: 'Go to next R', 8: 'Go to next R', 9: 'Go to next U', 10: -3}
# Tao list dem so lan o xuat hien
times = [0 for x in range(40)]
# Khoi tao ham random
from random import randint # Ham random integer
# Tao ham khi vao o CC
def go_CC(number,position):
    if number == 1:
        return 0
    elif number == 2:
        return 10
    else:
        return position
# Tao ham khi vao o CH
def go_CH(number,position):
    if number in range(1,7):
        return CH_cards[number]
    elif number in range(7,9):
        if position == 7:
            return 15
        elif position == 22:
            return 25
        else:
            return 5
    elif number == 9:
        if position == 22:
            return 28
        else:
            return 12
    elif number == 10:
        return position - 3
    else:
        return position

turn = 1 # Ham dem so luot choi
position = 0 # Vi tri ban dau tai GO
CC = 1 # Gia tri ban dau cua CC
CH = 1 # Gia tri ban dau cua CH
double = 0 # dem so lan 2 xuc xac giong nhau
# Chua tinh 3 lan xuc xac lien tiep giong nhau

while turn <= pow(10,6): # choi 1,000,000 luot
    dice_1 = randint(1,4)
    dice_2 = randint(1,4)
    if dice_1 == dice_2: # Kiem tra 2 xuc xac co giong nhau ko
        double += 1
    else:
        double = 0
    if double > 2:# 3 lan xuc xac giong nhau lien tuc thi vao tu
        position = 10
        times[position] += 1
    else:
        position = (position + dice_1 + dice_2) % 40
        if position == 30:  # Vao o G2J
            position = 10
        if position in [7, 22, 36]:  # Vao o CH
            position = go_CH(CH, position)
            CH = (CH + 1) % 16
        if position in [2, 17, 33]:  # Vao o CC
            position = go_CC(CC,position)
            CC = (CC + 1) % 16
        times[position] += 1
    turn += 1  # Tang so luot

# In vi tri 3 phan tu lon nhat cua time
print (times)
max_1 = max(times)
for i in range(40):
    if times[i] == max_1:
        print (i)
        times[i] = 0
max_2 = max(times)
for i in range(39):
    if times[i] == max_2:
        print (i)
        times[i] = 0
max_3 = max(times)
for i in range(38):
    if times[i] == max_3:
        print (i)