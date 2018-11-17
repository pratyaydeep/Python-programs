coins = [1,2,5,10,20,50,100]
n = 200
m = len(coins)
# Construct a table m x (n+1)
table = [[0 for x in range(m)] for x in range(n+1)]
print (table)
# Count the number of changing m coin in total into m different coins
# When n=0 there is only one way.
for i in range(m):
    table[0][i] = 1
for i in range(1,n+1):
    for j in range(m):
        if j>=1:
            x = table[i][j-1]
        else:
            x = 0
        if i>=coins[j]:
            y = table[i-coins[j]][j]
        else:
            y = 0
        table[i][j] = x + y
print (table)
print (table[n][m-1])