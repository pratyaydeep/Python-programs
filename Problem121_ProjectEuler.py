# All possible case is 16!
import math
all_pos = math.factorial(16)
# 15 turn thi can lan luot 8,9,10,11,12,13,14,15 dia xanh
from itertools import combinations
win_pos = 1
for i in range(8,15): # So dia xanh
    cases = list(combinations([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 15-i))
    for x in cases:
        product = 1
        for y in x:
            product *= int(y)
        win_pos += product

print (all_pos//win_pos)
