def cover(a, b, c, layer):
    first = 2*a*b + 2*b*c+ 2*c*a
    if layer == 1:
        return first
    else:
        return first + 4*(a + b + c)*(layer - 1) + 4*(layer - 2)*(layer-1)

limit = 2*pow(10,4)
C = [0 for i in range(limit)]
x = [a for a in range(1,limit) if cover(a,a,a,1)< limit]
for a in x:
    y = [b for b in range(a, limit) if cover(a,b,b,1)< limit]
    for b in y:
        z = [c for c in range(b, limit) if cover(a,b,c,1) < limit]
        for c in z:
            t = [d for d in range(1,100) if cover(a,b,c,d) < limit]
            for d in t:
                if cover(a,b,c,d) < limit:
                    C[cover(a,b,c,d)] += 1

print (C.index(1000))