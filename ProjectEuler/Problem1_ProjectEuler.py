desired_numbers = [x for x in range(1,1000) if x%3 ==0 or x%5 == 0]
total = 0
for number in desired_numbers:
    total += number
print (total)
