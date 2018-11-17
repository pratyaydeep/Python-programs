my_file = open("word.txt","r")
my_word = [ x.strip('"') for x in open('word.txt').read().split(',')]
my_file.close()
my_dict = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}
# Ham tinh gia tri tu
def value(word):
    result = 0
    for i in range(len(word)):
        result += my_dict[word[i]]
    return result
# List cac so tam giac
triangle_numbers = []
for i in range(1,51):
    triangle_numbers.append(int(i*(i+1)/2))
print (triangle_numbers)
count = 0
for i in range(len(my_word)):
    if value(my_word[i]) in triangle_numbers:
        count += 1
print (count)