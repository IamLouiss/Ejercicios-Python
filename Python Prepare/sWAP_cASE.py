def swap_case(s):
  swap = [letter.upper() if letter.islower() else letter.lower() for letter in s]
  s = "".join(swap)
  return(s)

if __name__ == '__main__':
  s = input()
  result = swap_case(s)
  print(result)