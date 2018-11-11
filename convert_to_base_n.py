def to_base(x, n):
  """
  A utility function to convert number x to base n

  Parameters
  ----------
  x : the integer to be converted
      x >= 0.
  n : the base number
      1 < n <= 10.

  Returns
  -------
  A string contains the representation of x in base n
  """
  if x == 0:
    return "0({})".format(n)
  
  result = []
  result.append('({})'.format(n))
  
  while x > 0:
    result. append(x % n)
    x = x//n
  
  return ''.join(map(str, result[::-1]))

if __name__ == "__main__":
  print("125 is written in base 2 as {}".format(to_base(125, 2)))
  print("15 is written in base 3 as {}".format(to_base(15, 3)))
  print("0 is written in base 5 as {}".format(to_base(0, 5)))


        
        
            

