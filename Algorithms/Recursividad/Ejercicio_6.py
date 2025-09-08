"""
Escriba una función recursiva para calcular el máximo común
divisor (m.c.d.) de dos números enteros dados aplicando
las propiedades recurrentes:

Si a > b entonces m.c.d.(a,b) = m.c.d.(a-b,b) 
Si a < b entonces m.c.d.(a,b) = m.c.d.(a,b-a) 
Si a = b entonces m.c.d.(a,b) = m.c.d.(b,a) = a = b
"""

def mcd(a : int, b : int):
  if a == b:
    return a
  if a > b:
    return mcd(a-b, b)
  elif a < b:
    return mcd(a, b-a)