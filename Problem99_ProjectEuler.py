my_file = open('base_exp.txt','r')
base = []
exponent = []
for i in range (1000):
    line = my_file.readline().strip("\n").split(',')
    base.append(line[0])
    exponent.append(line[1])
my_file.close()

# Y tuong la ta se chuyen cac base ve cung base la e roi tim exponent moi sau do so sanh
from math import log
new_exponent = []
for i in range(1000):
    a = log(float(base[i]))
    b = a * float(exponent[i])
    new_exponent.append(b)

print (new_exponent.index(max(new_exponent)) + 1)
