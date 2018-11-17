# Doc file
my_file = open('words.txt','r')
words = [ x.strip('"') for x in my_file.read().split(',')]
my_file.close()

# Hoan vi cua 1 tu
from itertools import permutations
def word_pair(word):
    per_word = [word]
    proper_words.remove(word)
    for i in list(permutations(word)):
        new_word = ''
        for j in range(len(word)):
            new_word += i[j]
        if new_word in proper_words:
            per_word.append(new_word)
            proper_words.remove(new_word)
    return per_word

# Mot danh gia nhe la cac tu phai co nhieu hon 1 va it hon 6 ki tu moi co hoan vi co nghia
proper_words = []
for i in range(len(words)):
    if 2 <= len(words[i]) <= 5:
       proper_words.append(words[i])

# List tat ca cac cap tu
pairs = []
while len(proper_words) != 0:
    new_list = word_pair(proper_words[0])
    if len(new_list) > 1:
        pairs.append(new_list)

# Ham tim so chinh phuong de gan gia tri cho cac pair.
def find_square(a_list):
    n = len(a_list[0])
    squares = [str(i ** 2) for i in range(1,350) if len(str(i ** 2)) == n]
    squares = squares[::-1]
    square = []
    for i in squares:
        check = True
        for j in range(n-1): # Kiem tra cac gia tri giong nhau co nhan so giong nhau
            for k in range(j+1,n):
                if a_list[0][j] == a_list[0][k] and i[j] != i[k]:# Kiem tra cac gia tri giong nhau co nhan so giong nhau
                    check = False
                if a_list[0][j] != a_list[0][k] and i[j] == i[k]:# Kiem tra cac gia tri khac nhau co nhan so khac nhau
                    check = False
        if check == True:
            square.append(i)
    for i in range(len(square)):
        dict = {}
        for j in range(n):
            dict[a_list[0][j]] = square[i][j]
        number = ''
        for j in range(n):
            number += dict[a_list[1][j]]
        if number in square:
            return max(int(square[i]), int(number))
            break
    else:
        return 0 # False

my_numbers = []
for i in range(len(pairs)):
    if find_square(pairs[i]) not in my_numbers:
        my_numbers.append(find_square(pairs[i]))

print (max(my_numbers))