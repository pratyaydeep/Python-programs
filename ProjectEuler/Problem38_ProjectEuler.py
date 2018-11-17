# function checks a 1 through 9 pandigital number
def pandigital(number):
    number = str(number)
    if len(number) == 9:
        for i in range(1,10):
            if str(i) not in number:
                return False
        else:
            return True
    else:
        return False
max = 918273645
for i in range(9000,10000):
    sum = int(str(i)+str(2*i))
    if pandigital(sum) and sum>max:
        max = sum
print (max)
