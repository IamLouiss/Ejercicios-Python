"""
Escriba un algoritmo que lea un número N y calcule e imprima el número
de dígitos de N.
"""

n = int(input("Ingrese un numero: ")) # Asumiendo que N siempre será positivo

if n == 0:
  print("El numero tiene 1 digito")
else:
  count = 0
  while n > 0:
    n //= 10
    count += 1
print(f"El numero tiene {count} digitos")