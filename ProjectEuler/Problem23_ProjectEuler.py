my_file = open("abundantnumbers.txt","r")
lines = my_file.readlines()
abundant_numbers = [int(x.strip("\n")) for x in lines]
my_file.close()
# Compute the sum of all numbers that cannot represent as sum of two abundant numbers
total = 0
for i in range(1,28124):
    if i<=23:
        total += i
    else:
        half = i//2
        j = 0
        while (abundant_numbers[j]<=half):
            if (i - abundant_numbers[j]) in abundant_numbers:
                break
            j += 1
        else:
            total += i
print (total)



