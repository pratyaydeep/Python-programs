# A desired number must be greater than 1 and less than 1 million
# Function check whether a number can be written as sum of fifth powers of its digits or not
def check(number):
    number = str(number)
    sum = 0
    for i in range(len(number)):
        sum += int(number[i]) ** 5
    if sum == int(number):
        return True
    else:
        return False
total = 0
for i in range(2,10**6):
    if check(i):
        total += i
print (total)