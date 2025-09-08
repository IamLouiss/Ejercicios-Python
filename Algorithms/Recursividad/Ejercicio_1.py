"""
Construya una función recursiva que calcule el valor de la combinatoria de 2 números enteros.
"""

def combination(n: int, k: int):
  if k == 0 or k == n:
    return 1
  if k > n:
    return 0
  
  return combination(n-1, k-1) + combination(n-1, k)