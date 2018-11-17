# Ham kiem tra xem 2 so ASCII xor voi nhau co ra co chu cai trong tieng anh ko?
def check_english(ascii1, ascii2):
    xor = ascii1 ^ ascii2
    if 32 <= xor <= 90:
        return True
    elif 97 <= xor <= 122:
        return True
    return False

# Tim chu truoc khi bi ma hoa
def decrypt(s, t): #s la mot ma ascii, t la key de giai ma
    return ''.join(chr(a ^ ord(b)) for a, b in zip(s, t))

f = open('cipher.txt')
cipher = f.read().strip().split(',')
f.close()
cipher = [int(x) for x in cipher]
eng_letters = range(97, 123)
# first letter of the encryption key
first_letter = set([])
# for loop to loop through a-z and cipher text
for j in eng_letters:
    for i in range(0, len(cipher), 3):
        first_letter.add(j)
        if not check_english(cipher[i], j):
            first_letter.remove(j)
            break

# second letter of the encryption key
second_letter = set([])

# for loop to loop through a-z and cipher text
for j in eng_letters:
    for i in range(1, len(cipher), 3):
        second_letter.add(j)
        if not check_english(cipher[i], j):
            second_letter.remove(j)
            break

# third character of the encryption key
third_letter = set([])

# for loop to loop through a-z and cipher text
for j in eng_letters:
    for i in range(2, len(cipher), 3):
        third_letter.add(j)
        if not check_english(cipher[i], j):
            third_letter.remove(j)
            break

# conver the first letter from ascii to character
first_letter = chr(list(first_letter)[0])

# convert the second letter from ascii to character
second_letter = chr(list(second_letter)[0])

# convert the third letter from ascii to character
third_letter = chr(list(third_letter)[0])

# string concatenation to find the encrypt key
encrypt_key = first_letter+second_letter+third_letter
# variable to store the decrypted string
plain_text = ''

# looping through the cipher text
for i in range(0, len(cipher), 3):
    plain_text += decrypt(cipher[i:i+3], encrypt_key)

# printing the sum of characters
sum = 0
for i in range(len(plain_text)):
    sum += ord(plain_text[i])
print (sum)