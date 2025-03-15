"""
Escriba un algoritmo que tome como entrada la base y la altura de un
triángulo, el radio de un círculo y determine si el triángulo tiene un área
mayor al círculo.
"""

import math
base, height = (input("Ingrese la base y antura del triangulo separado por un espacio: ").split())
base = float(base)
height = float(height)
radio = float(input("Ingrese el radio del circulo: "))
triangle_area = (base * height) / 2
circle_area = math.pi * radio**2
print(f"El area del triangulo es {triangle_area}\nEl area del circulo es {circle_area}")
print(f"El area del triangulo es mayor" if triangle_area > circle_area
      else "El area del circulo es mayor" if triangle_area < circle_area
      else "Las dos areas son iguales")