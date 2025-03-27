"""
Haga un algoritmo para una función que reciba dos parámetros N y
K y que retorne los K dígitos más a la izquierda de N. Por ejemplo,
extraerDigitos(542207, 2) debe retornar 54.
"""

# Forma manual

def reverse_number(number):
  number = int(number)
  r_number = 0
  while number > 0:
    r_number = (r_number * 10) + number % 10
    number //= 10
  return r_number

def k_digits(N, K):
  return reverse_number(reverse_number(N) % (10 ** K))

# Forma optimizada manual

def k_digits_optimized(N, K):
  N = int(N)
  return N // (10 ** (len(str(N)) - K))

# Forma directa

def k_digits_direct(N, K):
  return int(N[:K])

n = input("Ingrese un numero: ")
k = int(input("Ingrese el numero de digitos mas a la izquierda a extraer: "))
if k < 0 or k > len(n):
  print("El numero de digitos a extraer no puede ser negativo",
        "ni mayor a la cantidad de digitos del numero")
  exit()

print(k_digits(n, k))
print(k_digits_direct(n, k))
print(k_digits_optimized(n, k))