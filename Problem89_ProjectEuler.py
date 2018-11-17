my_file = open("roman.txt","r")
text = []
for i in range(1000):
    line = my_file.readline().strip('\n')
    text.append(line)
print (text)
my_file.close()

my_dict = {
    'M':1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
# Chuyen 1 so la ma thanh 1 so he 10
def convert_to_number(string):
    number = []
    for i in range(len(string)):
        number.append(my_dict[string[i]])
    sum = number[len(string)-1]
    for i in range(len(number) - 1):
        if number[i] < number[i+1]:
            sum -= number[i]
        else:
            sum += number[i]
    return sum

numbers = []
for i in range(1000):
    numbers.append(convert_to_number(text[i]))
print (numbers)

number_of_char = {
    9: 2, #IX
    8: 4, #VIII
    7: 3, #VII
    6: 2, #VI
    5: 1, #V
    4: 2, #IV
    3: 3, #III
    2: 2, #II
    1: 1, #I
    0: 0
}
# Chuyen 1 so he co so 10 ve so la ma theo dang ngan nhat
def count_char(n):
    a =  n // 1000
    b = (n % 1000) // 100
    c = (n % 100) // 10
    d =  n % 10
    count = a
    for i in [b,c,d]:
        count += number_of_char[i]
    return count

# Ta can tim so ki tu duoc rut gon di sau khi chuyen cac so ve dang gon nhat
result = 0
for i in range(1000):
    result += len(text[i]) - count_char(numbers[i])

print (result)