# function checks a 1 through 9 pandigital number
def pandigital(number):
    number = str(number)
    if len(number) == 9:
        for i in range(1,10):
            if str(i) not in number:
                return False
        else:
            return True
    else:
        return False
desired_product = []
for a in range(10,100):
    for b in range(100,1000):
        product = a * b
        if 1000 <= product and product <= 9999:
            sum = int(str(a)+str(b)+str(product))
            if pandigital(sum) and product not in desired_product:
                desired_product.append(product)
for a in range(1,10):
    for b in range(1000,10000):
        product = a * b
        if 1000 <= product and product <= 9999:
            sum = int(str(a) + str(b) + str(product))
            if pandigital(sum) and product not in desired_product:
                desired_product.append(product)
total = 0
for i in range(len(desired_product)):
    total += desired_product[i]
print(total)