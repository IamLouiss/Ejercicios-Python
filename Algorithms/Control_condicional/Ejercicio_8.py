"""
Un número de 4 cifras es felíz si los dos primeros dígitos son mayores que
los dos últimos dígitos. Por ejemplo 5612 es felíz porque 56 es mayor que
12. Un número de 4 cifras es creciente si cada dígito es mayor al anterior.
Por ejemplo 1569 es creciente porque 9 > 6 > 5 > 1. Todo número que es
felíz y creciente se dice que es un número muy felíz. Todo número que no es
felíz ni creciente se dice que es infelíz. Haga un algoritmo que tome como
entrada un número de 4 dígitos e imprima el tipo de número encontrado,
según la clasficicación descrita.
"""

n = int(input("Ingrese un numero de 4 digitos: "))

if len(str(n)) != 4: print("El numero debe ser de 4 digitos")
else:
  happy = False
  increasing = False
  first_two = n // 100
  last_two = n % 100
  
  happy = first_two > last_two
  while n > 0:
    aux = n % 10
    n //= 10
    if aux < (n % 10):
      increasing = False
      break

if happy and increasing:
  print("Muy feliz")
elif happy:
  print("Feliz")
elif increasing:
  print("Creciente")
else:
  print("Infeliz")