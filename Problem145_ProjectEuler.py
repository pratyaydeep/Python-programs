'''
Ta co nhan xet sau neu n co 2k chu so a1,a2,..,a2k thi cac so nay chia thanh k cap (a1,a2k),... co tong deu le va ko vuot qua 10
Do do cap dau co 20 cach chon cac cap sau co 30 cach chon
'''
count = 0
for k in range(1,5):
    count += 20*pow(30,k-1)
# Voi n le
# n = 3 thi a1a2a3 ta co a1+a3 le>10 a2<4:
count += 20*5
# n = 5 ko co
# n = 7 a1a2a3a4a5a6a7 ta co a1+a7 le >10, a2+a6 chan <10, a3+a5 le > 10, a4 < 4
count += 20*25*20*5
# n = 9 ko co
print (count)



