"""
Escriba un algoritmo que tome como entrada una secuencia de números
0 y 1 terminada en -1 que representan un número binario y calcule el
número decimal representado. Por ejemplo, si la secuencia es 1 0 0 1 0 1
-1, su algoritmo debe imprimir 37.
"""

binary_number = 0
decimal_number = 0
count = 0

while True:
  entry = int(input("Ingrese un numero entre 0 y 1 o -1 para finalizar: "))
  if entry == -1: break
  if entry == 0:
    binary_number *= 10
  elif entry == 1:
    binary_number = (binary_number * 10) + 1
  else:
    print("Ingrese un numero valido")
    continue
  count += 1
  
for i in range(count):
  current_number = binary_number % 10
  if current_number == 1:
    decimal_number += 2 ** i
  binary_number //= 10
print(f"El numero en decimal es: {decimal_number}")