"""
Escriba una función recursiva para calcular: 

1 + 1/2 + 1/3 + ... + 1/n

Asuma que recibe como parámetro el valor de n. 
"""

def sum_fraction_to_n(n : float):
  if n == 1:
    return 1.0
  return (1/n) + sum_fraction_to_n(n-1)