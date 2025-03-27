"""
Haga un algoritmo que permita determinar si un número N de 6 dígitos
contiene algún número de 3 dígitos capicúa. Por ejemplo, si N = 485992 no
hay números capicúas contenidos, pero N = 106562 si contiene uno (656).
"""

# Forma manual

def reverse(n):
  """Invierte un numero entero positivo"""
  n_reverse = 0
  while n > 0:
    n_reverse = (n_reverse * 10) + n % 10
    n //= 10
  return n_reverse

def arithmetic_capicua(n):
  """Verifica si hay un numero capicua de 3 digitos dentro de N, usando operaciones
  aritmeticas"""
  n = int(n)
  for i in range(4):
    digits = n % 1000
    if digits == reverse(digits): return True
    n //= 10
  return False

# Forma mas directa

def string_capicua(n):
  """Verifica si hay un numero capicua de 3 digitos dentro de N, usando slicing"""
  for i in range(4):
    substring = n[i:i+3]
    if substring == substring[::-1]: return True
  return False
    

n = input("Ingrese un numero positivo de 6 digitos: ")
if len(n) != 6:
  print("El numero debe tener 6 digitos")
  exit()
print("El numero contiene un numero capicua de 3 digitos" if string_capicua(n)
      else "No contiene ningun numero capicua de 3 digitos")