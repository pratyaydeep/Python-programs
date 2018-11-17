# Tim so du 28433×2^7830457+1 cho 10 ^ 10
# Truoc het ta tim so du cua 2^7830457 cho 5^10
# Theo LTE ta co 2*(4*5^9) - 1 chia het cho 5^10
# Do do ta chi can tim so du cua 2^17957 cho 10^10

remainder = 1
for i in range(1,17958):
    remainder = (2 * remainder) % pow(10,10)

print((28433 * remainder + 1) % pow(10,10))
