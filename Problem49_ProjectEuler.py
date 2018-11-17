def prime(n):
    if n <= 1:
        return False
    elif n < 9:
        for i in range(2,n):
            if n % i == 0:
                return False
                break
        else:
            return True
    else:
        for i in range(2,int(n ** 0.5)+1):
            if n % i == 0:
                return False
                break
        else:
            return True

from itertools import permutations
def permutation(n):
    my_list = list(permutations(str(n)))
    prime_number = []
    for i in range(len(my_list)):
        number = ""
        for j in range(4):
            number += my_list[i][j]
        if prime(int(number)) and int(number)>1000 and int(number) not in prime_number:
            prime_number.append(int(number))
    return prime_number
black_list = permutation(1487)
for n in range(1001,9999):
    if prime(n) and n not in black_list:
        prime_number = permutation(n)
        prime_number.sort()
        if len(prime_number) >= 3:
            for i in range(0, len(prime_number) - 2):
                for j in range(i + 1, len(prime_number) - 1):
                    for k in range(j + 1, len(prime_number)):
                        if 2 * prime_number[j] == prime_number[i] + prime_number[k]:
                            print(str(prime_number[i]) + str(prime_number[j]) + str(prime_number[k]))
                            break

