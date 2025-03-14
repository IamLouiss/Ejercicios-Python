"""
Escriba un algoritmo que reciba como entrada los coeficientes A, B y C
de una ecuación de segundo grado (Ax^2 + Bx +C = 0), e imprima por
pantalla los valores de x. Asuma que la ecuación siempre tiene solución
en números reales. Recuerde que la solución de una ecuación de segundo
grado viene dada por x = -b±√b^2-4ac / 2a.
"""

print("Ingrese los coeficientes de la ecuacion de segundo grado:")
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

x_1 = (-b + pow(pow(b,2) - (4*a*c),1/2)) / (2*a)
x_2 = (-b - pow(pow(b,2) - (4*a*c),1/2)) / (2*a)

if x_1 == x_2:
  print(f"x = {x_1}")
else:
  print(f"x_1 = {x_1}")
  print(f"x_2 = {x_2}")