# Doc du lieu tu file
my_file = open("names.txt","r")
roster = [ x.strip('"') for x in open('names.txt').read().split(',')]
roster.sort()
print (roster)
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
# Ham tinh gia tri ten
def value(name):
    result = 0
    for i in range(len(name)):
        result += my_dict[name[i]]
    return result
# Tinh ket qua
total = 0
for i in range(len(roster)):
    total += value(roster[i]) * (i+1)

print (total)
