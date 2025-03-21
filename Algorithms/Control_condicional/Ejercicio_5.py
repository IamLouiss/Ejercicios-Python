"""
Dados dos valores V1, V2 que forman un intervalo cerrado, y un valor X,
haga un algoritmo para determinar si X está dentro o fuera del intervalo.
"""

v1 = int(input("Ingrese el valor de V1: "))
v2 = int(input("Ingrese el valor de V2: "))
x = int(input("Ingrese el valor de x: "))

if v1 <= x <= v2:
  print(f"{x} esta en el intervalo cerrado [{v1},{v2}]")
else:
  print(f"{x} esta fuera del intervalo cerrado [{v1},{v2}]")