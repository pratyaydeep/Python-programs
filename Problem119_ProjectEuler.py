numbers = []
for i in range(8,200):
    for j in range(100):
        n = pow(i, j)
        digit = [int(x) for x in list(str(n))]
        if sum(digit) == i:
            numbers.append(n)

numbers.sort()
print (numbers[30])
# Ta chac chan dap an nay dung vi tong chu so cua so nay con chua vuot qua 200 (co it hon 20 chu so)