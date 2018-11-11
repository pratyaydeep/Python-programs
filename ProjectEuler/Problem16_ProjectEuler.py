# Ham nhan 2 voi mot chuoi
def multiply2(n):
    result = ""
    n = n [::-1]
    remember = 0
    for i in range(len(n)):
        a =  int(n[i])*2 + remember
        result += str(a%10)
        remember = a//10
    if remember == 1:
        result += "1"
    result = result[::-1]
    return result
# Ham tinh luy thua cua 2
def power(n):
    if n == 0:
        return "1"
    else:
        return multiply2(power(n-1))
import sys
sys.setrecursionlimit(1500)
result = (power(1000))
total = 0
for i in range(len(result)):
    total += int(result[i])
print (total)