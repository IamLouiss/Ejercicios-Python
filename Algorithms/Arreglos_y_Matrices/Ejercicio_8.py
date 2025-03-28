"""
Haga una función que tome como entrada un arreglo de enteros A y un
número K y determine si existen dos valores de A que sumados sean
iguales a K. Por ejemplo, si A = {4, -1, 6, 8, 10, 3} y K = 2, la función
debe retornar verdadero ya que -1 + 3 = 2.
"""

def two_added_numbers_equal_k(numbers_list : list[int], k : int) -> bool:
  for i in range(len(numbers_list)):
    for j in range(len(numbers_list)):
      if i == j: continue
      if numbers_list[i] + numbers_list[j] == k:
        return True
  return False

# Version mas eficiente usando conjuntos

# def two_added_numbers_equal_k(numbers_list: list[int], k: int) -> bool:
#   seen = set()
#   for num in numbers_list:
#       complement = k - num
#       if complement in seen:
#           return True
#       seen.add(num)
#   return False

A = [4, -1, 6, 8, 10, 3]
k = 2
print(two_added_numbers_equal_k(A, k))