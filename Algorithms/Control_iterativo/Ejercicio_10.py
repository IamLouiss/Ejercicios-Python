"""
Escriba un algoritmo que imprima por pantalla en borde de un cuadrado de
lados de tamaño N. Por ejemplo, si N = 5, el algoritmo debería imprimir:
XXXXX
X   X
X   X
X   X
XXXXX
"""

n = int(input("Ingrese un numero N: "))

for i in range(n):
  for j in range(n):
    if (i == 0 or i == n-1) or (j == 0 or j == n-1): print("X", end="")
    else: print(end=" ")
  print()