if __name__ == '__main__':
  s = input()
  alphanumeric = False
  alphabetical = False
  digits = False
  lowercase = False
  uppercase = False

  for i in range(len(s)):
    if s[i].isalnum():
      alphanumeric = True
    if s[i].isalpha():
      alphabetical = True
    if s[i].isdigit():
      digits = True
    if s[i].islower():
      lowercase = True
    if s[i].isupper():
      uppercase = True

  print(alphanumeric)
  print(alphabetical)
  print(digits)
  print(lowercase)
  print(uppercase)