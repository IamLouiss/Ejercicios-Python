"""
Haga un algoritmo que reciba como entrada un número entre 1 y 12 e
imprima el nombre del mes correspondiente. Tome en cuenta posibles
valores erróneos en la entrada.
"""

n = int(input("Ingrese un numero entre 1 y 12: "))

if 1 <= n <= 12:
  months = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio, ", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
  print(f"El mes es {months[n-1]}")
else:
  print("El numero no esta entre 1 y 12")