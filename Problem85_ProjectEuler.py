# So hinh chu nhat con voi hinh chu nhat a x b la a(a+1)b(b+1)/4
def nearest(a):
    b = 8 * pow(10,6) / (a * (a + 1))
    c = (-1 + (1 + 4 * b) ** 0.5) // 2
    return c

min = 1000
S = 0
n = 0
for i in range(1,60):
    j = nearest(i)
    if abs(8 * pow(10,6) - i * (i + 1) * j * (j + 1)) < min:
        min = abs(8 * pow(10,6) - i * (i + 1) * j * (j + 1))
        S = i * j
        n = i
print (S)
print (n)