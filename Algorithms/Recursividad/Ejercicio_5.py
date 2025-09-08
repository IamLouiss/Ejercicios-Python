"""
Escriba un algoritmo recursivo que halle la suma de
los primeros N números naturales. 
"""

def sum_to_n(n : int):
  if n == 0:
    return 0
  return n + sum_to_n(n-1)