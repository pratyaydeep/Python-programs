# Khoi tao day ban dau
F_numbers = [1,2]
x = 1
# Viet tiep day cho den so lon nhat ko vuot qua 4 trieu
while (F_numbers[x] <= 4* (10 ** 6)):
    F_numbers.append(F_numbers[x] + F_numbers[x-1])
    x +=1
# Tinh tong cac phan tu chan ko vuot qua 4 trieu
F_evennumbers = [x for x in F_numbers if x%2 ==0 and x <= 4* (10 ** 6)]
total = float(0)
for number in F_evennumbers:
    print (number)
    total += float(number)
print (total)