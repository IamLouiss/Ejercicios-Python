"""
Escriba un algoritmo utilizando un ciclo para que calcule el valor aproximado
de π usando la serie: π = 4 - 4/3 + 4/5 - 4/7 + 4/9 ... +- 4/n.
"""

n = int(input("Ingrese un numero impar mayor o igual que 1: "))

pi = 0
sign = 1
for denominator in range(1, n+1, 2):
  pi += sign * (4/denominator)
  sign *= -1
print(f"El valor aproximado de pi es {pi}")