"""
Haga una función que tome como entrada un string y retorne verdadero si
es capicúa
"""

# Usando slicing

def slicing_capicua(string : str) -> bool:
  return string == string[::-1]

# Forma manual

def manual_capicua(string : str) -> bool:
  left = 0
  right = len(string) - 1
  while left < right:
    if string[left] != string[right]: return False
    left += 1
    right -= 1
  return True

print(slicing_capicua("asdsa"))
print(manual_capicua("asdsa"))
print(slicing_capicua("asd"))
print(manual_capicua("asd"))