for a in range(250,500):
    for b in range(a):
        if a * b % 2 == 0:
            c = (a**2 + b**2) ** 0.5
            if a + b + c == 1000:
                print (a * b * c)
