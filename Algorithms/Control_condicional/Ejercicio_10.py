"""
Haga un algoritmo que tome como entrada un número menor a 100 y
determine si es primo (recuerde que un número N es primo si sus únicos
divisores son 1 y N).
"""

n = int(input("Ingrese un numero positivo mayor que 1 y menor que 100: "))
if 1 < n < 100:
  primo = True
  for i in range(2, n):
    if n % i == 0 :
      primo = False
      break
  if primo:
    print("El numero es primo")
  else:
    print("El numero no es primo")
else:
  print("El numero no esta en el rango correcto")