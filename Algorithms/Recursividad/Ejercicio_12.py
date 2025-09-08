"""
Escriba una función recursiva que invierta los dígitos de un
número entero, empleando operaciones sobre números enteros. 
Ejemplo: 653 a 356. 
"""

def reverse(n: int, lenght = None):
  if lenght is None:
    lenght = 0
    aux = n
    while aux > 0:
      lenght += 1
      aux //= 10
  if n < 10:
    return n
  return (n % 10) * 10**(lenght-1) + reverse(n//10, lenght-1)