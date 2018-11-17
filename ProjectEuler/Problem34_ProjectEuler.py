from math import factorial
total = 0
def check(number):
    number = str(number)
    sum = 0
    for i in range(len(number)):
        sum += factorial(int(number[i]))
    if sum == int(number):
        return True
    else:
        return False
for i in range(3,10**6):
    if check(i):
        total += i
print (total)