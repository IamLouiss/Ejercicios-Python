"""
Haga una función que tome como entrada un arreglo y retorne el máximo
valor del mismo
"""

def max_element(number_list : list):
  if not number_list:
    return None
  max = number_list[0]
  for element in number_list:
    if element > max: max = element
  return max

print(max_element([1, 10, 3 ,4]))
print(max_element([]))