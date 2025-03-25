"""
Escriba un algoritmo que lea un número real x, un número entero n y los coeficientes
reales a_i de un polinomio p(x) = a_0x^0 +a_1x^1 +a_2x^2 ...a_n-1x^(n-1)
y calcule el valor del polinomio para el x dado. Por ejemplo, si x = 2, n = 3
y los coeficientes son 2, -1, 3, el polinomio es p(x) = 2 -x + 3x^2, y debe
imprimir el valor 12.
"""

x = float(input("Ingrese el valor de x: "))
n = int(input("Ingrese el grado del polinomio: "))
if n < 0:
  print("El grado del polinomio debe ser positivo")
  exit()
result = 0

for i in range(n):
  coefficient = float(input(f"Ingrese el valor del coeficiente a_{i}: "))
  result += coefficient * (x ** i)
print(f"En x = {x} el polinomio vale {result}")