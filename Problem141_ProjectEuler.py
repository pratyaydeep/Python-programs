# (r,q,d) = (rb2,rab,ra2) b<a

def square_number(n):
    if round(n ** 0.5) ** 2 == n:
        return True
    else:
        return False

progressive_square = []
limit = pow(10,12)
for a in range(1,int(pow(limit,1/3))+1):
    for b in range(1,a):
        for r in range(1,int(pow(limit/(b*pow(a,3)),1/2))+1):
            n = r*pow(b,2) + b*pow(a,3)*pow(r,2)
            if n < limit and square_number(n) and n not in progressive_square:
                progressive_square.append(n)

print (sum(progressive_square))