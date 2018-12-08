"""
https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
def multiple_3_or_5(n):
    """
    A utility function to calculate the sum of all multiples of 3 or 5 below n
    Parameters
    ---------------
    n: a positive integer 
    Returns
    ------------
    The calculated sum
    """
    
    total = 0
    desired_numbers = [x for x in range(1,n) if x%3 == 0 or x%5 == 0]
    
    return sum(desired_numbers)

if __name__ == "__main__":
    n = 1000
    print("sum of all the multiples of 3 or 5 below {} is {}".format(n, multiple_3_or_5(n)))
