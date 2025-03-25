"""
Escriba un algoritmo que imprima por pantalla en borde de cuadrados de
tamaño impar desde N hasta 1 insertados uno dentro de otro. Por ejemplo,
si N = 7 y N = 9 debe imprimir:

XXXXXXX   XXXXXXXXX
X     X   X       X
X XXX X   X XXXXX X
X X X X   X X   X X
X XXX X   X X X X X
X     X   X X   X X
XXXXXXX   X XXXXX X
          X       X
          XXXXXXXXX
"""

n = int(input("Ingrese N (impar): "))
center = n // 2

for row in range(n):
  for column in range(n):
      distance = max(abs(row - center), abs(column - center))
      if (center - distance) % 2 == 0:
           print("X", end="")
      else:
          print(" ", end="")
  print()