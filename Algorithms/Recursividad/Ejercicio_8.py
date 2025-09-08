"""
Escriba una función recursiva para calcular la potencia
de un número real elevado a un entero positivo, partiendo de:

x^0 = x
x^n = (x*x)^(n/2) si n > 0 y es par 
x^n = x*(x^(n-1)) si n > 0 y es impar 
"""

def x_power_n(x: float, n: int):
  if n == 0:
    return 1.0
  if n % 2 == 0:
    return x_power_n(x*x, n // 2)
  else:
    return x * x_power_n(x, n-1)