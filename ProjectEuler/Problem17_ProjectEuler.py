my_dict = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety"
}
# Cach doc tung so
def translate(n):
    result = ""
    if n != 0:
        a = n//100
        n = n - a*100
        c = n % 10
        b = n - c
    if a != 0:
        a = str(a)
        result += my_dict[a] + "hundred"
    if b > 10:
        result += "and"
        b = str(b)
        result += my_dict[b]
        if c != 0:
            c = str(c)
            result += my_dict[c]
    elif b == 0:
        if c != 0:
            result += "and"
            c = str(c)
            result += my_dict[c]
    else:
        result += "and"
        if c == 0 :
            result += "ten"
        else:
            d = str(b+c)
            result += my_dict[d]
    return len(result)

total = 0
for i in range(1,1000):
    total += translate(i)
total += 11 - 3*99
print (total)