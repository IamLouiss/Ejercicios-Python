"""
Haga un algoritmo que imprima “Capicua” si un número de entrada de 5
dígitos es capicua, o “No lo es” en caso contrario. Un número es capicua
si se escribe igual al derecho y a revés. Por ejemplo, 545 es un número
capicua.
"""

num = input("Ingrese un numero de 5 digitos: ")

i, j = 0, (len(num)-1)
capicua = True
while i < j:
  if num[i] != num[j]:
    capicua = False
    break
  i += 1
  j -= 1

if capicua:
  print("Capicua")
else:
  print("No lo es")

## Forma alternativa

# print("Capicua" if num == num[::-1]
#       else "No lo es")