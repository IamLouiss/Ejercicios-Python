"""
Dado un número N, desarrolle una función recursiva que calcule
la secuencia de números de Fibonacci para N. 
"""

def fibonacci(n : int):
  if n <= 1:
    return n
  return fibonacci(n-2) + fibonacci(n-1)