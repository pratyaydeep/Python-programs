# Xac dinh tap uoc nguyen to cua mot so
n = int(input("Input a positive integer:"))

def LPF(n):
    if n > 1:
        i = 2
        while(n > i):
            if n % i == 0:
                return LPF(n/i)
            else:
                i += 1
        else:
            return n

print (LPF(n))